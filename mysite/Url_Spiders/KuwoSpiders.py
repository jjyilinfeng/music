import requests
from lxml import etree
'''********************************************酷我音乐爬虫************************************************'''
def KuwoSpider(url):
    Download_Msg = {
        'music_url': "",
        'music_name': "",
        'music_singer': "",
        'music_album': "",
        'music_lyric': "",
        'music_image_url': "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596979657869&di=619cc58a42cbaa56f68af9f3e6e82a55&imgtype=0&src=http%3A%2F%2Fpic.qqtn.com%2Fup%2F2017-7%2F2017071716392766525.jpg"
    }
    response = requests.get(url)
    html = etree.HTML(response.text)
    Download_Msg['music_name'] = html.xpath("//p[@class='song_name flex_c']/span/text()")
    Download_Msg['music_name'] = Download_Msg['music_name'][0].strip()
    Download_Msg['music_singer'] = html.xpath("//p[@class='artist_name flex_c']/span/text()")[0]
    Download_Msg['music_album'] = html.xpath("//p[@class='song_info']/span[@class='tip album_name']/text()")[0]
    t = url.index("ail/")
    str = url[t + 4:]
    url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1582894271662&reqId=ff4d2920-5a28-11ea-a40f-c96cc7a8aad1'.format(str)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
        'csrf': 'RUJ53PGJ4ZD',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD'
    }
    try:
        response = requests.get(url, headers=headers).json()
        Download_Msg['music_url'] = response['url']
    except:
        Download_Msg['music_url'] = '获取链接失败'
    return Download_Msg