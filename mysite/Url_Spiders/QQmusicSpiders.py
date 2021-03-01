import requests
from lxml import etree
import json
import html
'''********************************************QQ音乐爬虫************************************************'''
class QQMusicSpider():
    def __init__(self,songmid):
        self.songmid = songmid
        self.Download_Msg = {
        'music_url': "",
        'music_name': "",
        'music_singer': "",
        'music_album': "无",
        'music_lyric': "",
        'music_image_url': ""
        }#歌曲URL、歌曲名、歌手、专辑名、歌词、封面图地址
        self.lyric_headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'https://y.qq.com',
            'Referer': 'https://y.qq.com/n/yqq/song',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }

    def music_msg_spider(self):
        t = self.songmid.index("song/")
        h = self.songmid.index('.html')
        response = requests.get(self.songmid)
        self.songmid = self.songmid[t + 5:h]
        self.Download_Msg['music_url'] = self.sprider()

        htmL = etree.HTML(response.text)
        self.Download_Msg['music_name'] = htmL.xpath("//h1[@class='data__name_txt']/text()")[0]
        self.Download_Msg['music_singer'] = ",".join(htmL.xpath("//div[@class='data__singer']/a/text()"))
        self.Download_Msg['music_album'] = htmL.xpath("//ul[@class='data__info']/li/a/text()")[0]
        self.Download_Msg['music_image_url'] = htmL.xpath("//span[@class='data__cover']/img/@src")[0]
        music_id = htmL.xpath("//div[@class='data__actions']/a/@data-id")[0]
        item_res = requests.get(
            'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid={}&-=jsonp1&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(
                music_id), headers=self.lyric_headers)
        item_html = item_res.json()
        self.Download_Msg['music_lyric'] = html.unescape(item_html['lyric'])

        lyric_file = open("lyric.lrc", "w+",encoding = 'utf-8')
        lyric_file.write(self.Download_Msg['music_lyric'])
        lyric_file.close()

        return self.Download_Msg
    def sprider(self):
            URL = "获取资源失败，可能是因为没有版权"
            data='%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%224776407682%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%224776407682%22%2C%22songmid%22%3A%5B%22'+self.songmid+'%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'
            url='https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey23927290711706184&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%s'%data
            headers={
                'Referer':'https://y.qq.com/portal/player.html',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }
            response=json.loads(requests.get(url=url,headers=headers).content.decode('utf-8'))['req_0']['data']
            if response['midurlinfo'][0]['purl']!='':
                URL=response['sip'][0]+response['midurlinfo'][0]['purl']

            return URL

if __name__ == "__main__":
    spider = QQMusicSpider("https://y.qq.com/n/yqq/song/274114008_num.html#stat=y_new.index.toplist.songname")
    # print(spider.music_msg_spider())