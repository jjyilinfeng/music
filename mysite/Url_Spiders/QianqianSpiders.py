import requests
from lxml import etree

'''********************************************千千音乐爬虫************************************************'''
def Qianqianspider(url):
    Download_Msg = {
        'music_url': "",
        'music_name': "",
        'music_singer': "",
        'music_album': "",
        'music_lyric': "",
        'music_image_url': ""
    }
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    Download_Msg['music_name'] = html.xpath("//h2[@class='songpage-title clearfix']/span/text()")[0]
    Download_Msg['music_singer'] = html.xpath("//p[@class='artist-box']/span[@class='artist']/span[@class='author_list']/a/text()")[0]
    Download_Msg['music_album'] = html.xpath("//div[@class='song-info-box fl']/p[@class='album desc']/a/text()")[0]
    Download_Msg['music_image_url'] = html.xpath("//div[@class='song-img-box pr']/img/@src")[0]

    id = url.rsplit('/', 1)[1]
    url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid={}&from=web'.format(id)
    html = requests.get(url).json()
    Download_Msg['music_url'] = html['bitrate']['file_link']
    return Download_Msg