import requests
import json
from lxml import etree

def QQMusic(music_name,page,page_items):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'https://y.qq.com',
        'Referer': 'https://y.qq.com/n/yqq/song',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    res = requests.get(
        'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=67198573060150304&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p={}&n={}&w={}&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(
            page, page_items, music_name), headers=headers)
    search_html = res.json()
    items = search_html['data']['song']['list']
    print(items)
    data_music = []
    for i in items:
        data = '%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%224776407682%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%224776407682%22%2C%22songmid%22%3A%5B%22' + \
               i['mid'] + '%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'
        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey23927290711706184&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%s' % data
        url2 = 'https://y.qq.com/n/yqq/song/' + i['mid'] + ".html"
        music_msg = ["", "", "", "", ""]
        music_msg[0] = "QQ音乐"
        music_msg[1] = i['name']
        music_msg[2] = '/'.join(x['name'] for x in i['singer'])

        response = json.loads(requests.get(url=url, headers=headers).content.decode('utf-8'))['req_0']['data']
        if response['midurlinfo'][0]['purl'] != '':
            URL = response['sip'][0] + response['midurlinfo'][0]['purl']
            music_msg[3] = URL
        else:
            music_msg[3] = '-' * 20
        data_music.append(music_msg)
        response2 = requests.get(url2)
        html = etree.HTML(requests.get(url2).text)
        music_msg[4] = "http:" + html.xpath("//span[@class='data__cover']/img/@src")[0]
    return data_music


if __name__ == "__main__":
    print(QQMusic("十里香",1,10))