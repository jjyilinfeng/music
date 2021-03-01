import requests
import re

'''********************************************酷狗音乐爬虫************************************************'''


class KugouSpider:
    def __init__(self, url):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'

        }
        t = url.index("hash=")
        p = url.index("&album")
        url = url[t + 5:p]
        self.url_Str = url

    def get_music_playurl(self):
        self.url2 = 'https://wwwapi.kugou.com/yy/index.php?'
        hash_result = self.url_Str
        self.data2 = [
            'r=play/getdata',
            'callback=jQuery1910026577801017397817_1596164131720',
            'hash={}'.format(hash_result),
            'album_id=',
            'dfid=0zPSYM1q2qH90xArIr1yOGtc',
            'mid=5cd316b98602d9b29f31085c96e6c682',
            'platid=4',
            '_=1596164131722'
        ]
        u = "&".join(self.data2)
        response = requests.get(self.url2 + u, headers=self.headers)
        html = response.text
        Download_Msg = {
            'music_url': "",
            'music_name': "",
            'music_singer': "",
            'music_album': "",
            'music_lyric': "",
            'music_image_url': ""
        }  # 歌曲URL、歌曲名、歌手、专辑名、歌词、封面图地址

        url = re.search('play_url":"(.*?)"', html).group(1)
        Download_Msg['music_url'] = url.replace('\\', '')
        Download_Msg['music_name'] = re.search('song_name":"(.*?)"', html).group(1).encode('utf8').decode(
            'unicode_escape')
        Download_Msg['music_singer'] = re.search('author_name":"(.*?)"', html).group(1).encode('utf8').decode(
            'unicode_escape')
        Download_Msg['music_album'] = re.search('album_name":"(.*?)"', html).group(1).encode('utf8').decode(
            'unicode_escape')
        lyrics = re.search('lyrics":"(.*?)"', html).group(1).encode('utf8').decode('unicode_escape')
        try:
            Download_Msg['music_lyric'] = lyrics[lyrics.index("[00"):]
        except:
            Download_Msg['music_lyric'] = ""
        Download_Msg['music_image_url'] = re.search('img":"(.*?)"', html).group(1).replace('\\', '')

        return Download_Msg


if __name__ == "__main__":
    spider = KugouSpider("https://www.kugou.com/song/#hash=5B7F8DCFB2CB2240D5EE8E917A0B1AEF&album_id=33194412")
    print(spider.get_music_playurl())
