import json
import requests
from lxml import etree

'''********************************************5sing音乐爬虫************************************************'''


def FivesingSpider(url):
    Download_Msg = {
        'music_url': "",
        'music_name': "",
        'music_singer': "",
        'music_album': "无",
        'music_lyric': "",
        'music_image_url': ""
    }
    u = requests.get(url).text
    html = etree.HTML(u)
    Download_Msg['music_name'] = html.xpath("//div[@class='view_tit']/h1/text()")[0]
    Download_Msg['music_singer'] = html.xpath("//ul[@class='lt mb15']/li[1]/a/text()")[0]
    Download_Msg['music_image_url'] = html.xpath("//div[@class='user_tx']/a/img/@src")[0]
    music_lyric = html.xpath("//div[@class='lrc_info_clip lrc-tab-content']/div/text()")
    music_lyric.pop()
    music_lyric.pop(0)

    id = url.rsplit('/', 1)[1].split('.')[0]
    if 'com/fc' in url:
        url = 'http://service.5sing.kugou.com/song/getsongurl?songid={}&songtype=fc&from=web'.format(id)
        music_lyric[0] = music_lyric[0].split()[0]
        music_lyric.pop()
        Download_Msg['music_lyric'] = ' '.join(music_lyric).replace(' ', '\n')
    elif 'com/yc' in url:
        url = 'http://service.5sing.kugou.com/song/getsongurl?songid={}&songtype=yc&from=web'.format(id)
        music_lyric[0] = music_lyric[0].split()[0]
        music_lyric[-1] = music_lyric[-1].split()[0]
        Download_Msg['music_lyric'] = ' '.join(music_lyric).replace(' ', '\n')
    else:
        url = ""

    # 写入歌词
    lyric_file = open("lyric.lrc", "w+")
    lyric_file.write(Download_Msg['music_lyric'])
    lyric_file.close()

    html = requests.get(url).text[1:-1]
    result = json.loads(html)
    Download_Msg['music_url'] = result['data']['hqurl']
    if not Download_Msg['music_url']:
        Download_Msg['music_url'] = result['data']['hqurl'] + result['data']['lqurl']
    return Download_Msg


if __name__ == "__main__":
    print(FivesingSpider("http://5sing.kugou.com/fc/17560521.html"))