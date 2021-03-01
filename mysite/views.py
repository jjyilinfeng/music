from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import FileResponse
import datetime
import json
import socket

# 爬虫文件
from .Url_get import main
from .Songs_get import start

# 数据库模板文件
from mysite import models

# 彩蛋钥匙
egg_key = False


def get_window_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()

    return ip


# 获取本地局域网IP地址
local_ip = get_window_ip()


# 根据歌曲链接获取音乐界面
def index(request):
    # data初始化
    data = {}

    data['local_ip'] = local_ip
    # print(local_ip)

    # Aplayer播放器初始化
    data['player_url'] = '""'
    data['player_music_name'] = '""'
    data['player_music_singer'] = '""'
    data['player_music_image'] = '""'
    if request.method == 'POST':
        # 得到输入的音乐地址值
        in_url = request.POST.get('url')

        # 如果为空就返回
        if in_url == "":
            return render(request, 'index.html', data)

        # 执行爬虫将信息传递给msg
        msg = main(in_url)

        # 将搜索的关键词记录到数据库
        if msg['music_name'] != '当前歌曲不支持获取':
            if models.music_key_statistics.objects.filter(music_key=msg['music_name']).exists():
                Music_key = models.music_key_statistics.objects.get(music_key=msg['music_name'])
                Music_key.music_key_times += 1
                Music_key.save()
            else:
                Music_key = models.music_key_statistics()
                Music_key.music_key = msg['music_name']
                Music_key.music_key_times = 1
                Music_key.save()

        # 爬到的数据传递给data
        data['url'] = msg['music_url']
        data['music_name'] = msg['music_name']
        data['music_singer'] = msg['music_singer']
        data['music_info'] = msg['music_album']
        data['music_lyric'] = msg['music_lyric']
        data['music_image'] = msg['music_image_url']

        # Aplayer播放器信息传递
        data['player_url'] = json.dumps(msg['music_url'])
        data['player_music_name'] = json.dumps(msg['music_name'])
        data['player_music_singer'] = json.dumps(data['music_singer'])
        data['player_music_image'] = json.dumps(msg['music_image_url'])
        data['player_lyric'] = json.dumps(msg['music_lyric'])

    return render(request, 'index.html', data)


# lyric下载界面
def lyric_download(request):
    file = open('lyric.lrc', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment'
    return response


# 根据关键词搜索音乐界面
def songs(request):
    d = []
    in_song = ""
    song_type = "网易云音乐"
    user_ip = ""
    data = {
        'music_type': song_type,
        'local_ip': local_ip
    }
    # 音乐序号
    s = 1
    if request.method == 'POST':
        # 获取表格带来的信息：输入的音乐关键字、音乐库类型
        in_song = request.POST.get('song')
        song_type = request.POST.get('music_type')
        page = request.POST.get('page')
        song_num = request.POST.get('song_num')

        # 判断输入值是否为空，空就返回
        if in_song == "":
            return render(request, 'songs_get.html', data)

        # 获取用户访问IP
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            user_ip = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            user_ip = request.META.get("REMOTE_ADDR")

        # 将关键词传输到关键词统计数据库中
        if models.music_key_statistics.objects.filter(music_key=in_song).exists():
            Music_key = models.music_key_statistics.objects.get(music_key=in_song)
            Music_key.music_key_times += 1
            Music_key.save()
        else:
            Music_key = models.music_key_statistics()
            Music_key.music_key = in_song
            Music_key.music_key_times = 1
            Music_key.save()

        # 清除上次IP访问所生成的歌曲信息
        delete_Data = models.Music.objects.filter(user_ip=user_ip)
        delete_Data.delete()

        # 执行爬虫程序信息传递给d
        d = start(in_song, song_type, page, song_num)

        # 将爬到的数据导入到数据库中
        for i in d:
            mus = models.Music()
            mus.song_come = i[0]
            mus.song_name = i[1]
            mus.song_singer = i[2]
            mus.song_link = i[3]
            try:
                mus.song_img_link = i[4]
            except Exception:
                pass
            mus.user_ip = user_ip
            mus.song_no = s
            s += 1
            if '----------------' in mus.song_link:
                mus.song_link = '获取资源失败，可能是没有版权'
            mus.save()

        # 将符合用户IP查询的歌曲信息传递给网页
        songs = models.Music.objects.filter(user_ip=user_ip)
        data = {
            'songs': songs,
            'music_type': song_type,
            'in_music': in_song,
            'local_ip': local_ip,
        }
    return render(request, 'songs_get.html', data)


# 测试数据界面
def test(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")

    print("ip:", ip)
    return render(request, 'test.html')


# 使用说明界面
def website_manual(request):
    data = {}
    data['local_ip'] = local_ip
    return render(request, 'website_manual.html', data)


# 留言板界面
def message(request):
    messages = models.Message.objects.all()
    return render(request, 'message.html', {'messages': messages, 'local_ip': local_ip})


# 留言界面
def create_message(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        title = request.POST.get("subject")
        mail = request.POST.get("email")
        content = request.POST.get("message")
        publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = models.Message()
        message.mail = mail
        message.content = content
        message.title = title
        message.publish = publish
        message.username = username
        message.save()
        return HttpResponseRedirect('/home/message/')
    return render(request, 'create_message.html')


# 关键词统计界面
def music_key_statistics(request):
    items = models.music_key_statistics.objects.order_by("-music_key_times")
    data = {
        'items': items
    }
    return render(request, 'Music_Key_Statistics.html', data)


# 错误界面
def bad_request(request, exception, template_name='404.html'):
    return render(request, template_name)


def permission_denied(request, exception, template_name='404.html'):
    return render(request, template_name)


def page_not_found(request, exception, template_name='404.html'):
    data = {}
    data['local_ip'] = local_ip
    global egg_key
    egg_key = True
    return render(request, template_name, data)
