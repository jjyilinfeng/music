import requests
from lxml import etree
'''********************************************荔枝FM爬虫************************************************'''
def LizhifmSpider(url):
    Download_Msg = {
        'music_url': "",
        'music_name': "",
        'music_singer': "",
        'music_album': "无",
        'music_lyric': "无",
        'music_image_url': ""
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    id = url.rsplit('/', 1)[1]
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    Download_Msg['music_name'] = html.xpath("//div[@class='audioInfo']/h1/text()")[0]
    Download_Msg['music_singer'] = html.xpath("//p[@class='radioAttr fontYaHei']/span/a/text()")[0]
    Download_Msg['music_image_url'] = html.xpath("//div[@class='audioCover left']/img/@src")[0]
    url = 'http://www.lizhi.fm/media/url/{}'.format(id)
    html = requests.get(url, headers=headers).json()
    Download_Msg['music_url'] = html['data']['url']
    return Download_Msg

if __name__ == "__main__":
    print(LizhifmSpider("https://www.lizhi.fm/551550/5126699846247448582"))