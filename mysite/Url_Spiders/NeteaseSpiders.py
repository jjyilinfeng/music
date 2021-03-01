import requests
from lxml import etree
import json

def NeteaseSpider(url):
    headers = {
        'Referer': 'https://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }

    Download_Msg = {
        'music_url': "",
        'music_name': "",
        'music_singer': "",
        'music_album': "",
        'music_lyric': "",
        'music_image_url': ""
    }
    if not '#' in url:
        q = url.index("com/")
        url = url[:q+4] + "#/" + url[q+4:]

    str = url[url.index("id=") + 3:]
    Download_Msg['music_url'] = "http://music.163.com/song/media/outer/url?id=" + str
    lyric_url = "http://music.163.com/api/song/lyric?id={}&lv=1&kv=1&tv=-1".format(str)

    try:
        Download_Msg['music_lyric'] = json.loads(requests.get(lyric_url,headers=headers).text)['lrc']['lyric']
    except:
        Download_Msg['music_lyric'] = "纯音乐，请欣赏"
    #歌词写入
    lyric_file = open("lyric.lrc", "w+")
    lyric_file.write(Download_Msg['music_lyric'])
    lyric_file.close()

    t = url.index("/#")
    u = url[:t]+url[t+2:]
    response = requests.get(u)
    html = etree.HTML(response.text)
    Download_Msg['music_name'] = html.xpath("//em[@class='f-ff2']/text()")[0]
    Download_Msg['music_singer'] = html.xpath("//p[@class='des s-fc4']/span/a/text()")[0]
    Download_Msg['music_album'] = html.xpath("//p[@class='des s-fc4']/a/text()")[0]
    Download_Msg['music_image_url'] = html.xpath("//div[@class='u-cover u-cover-6 f-fl']/img/@src")[0]

    return Download_Msg
if __name__ == '__main__':
    print(NeteaseSpider("https://music.163.com/#/song?id=1343016814"))