import requests
import re
import json


# 去掉<em>标签
def Drop_Em(str):
    try:
        p1 = str.index("<em>")
        p2 = str.index("</em>")
        return str[p1 + 4:p2]
    except:
        return str


def KugouMusic(music_name, page, pagesize):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }

    search_url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery11240251602301830425_1548735800928&keyword={}&page={}&pagesize={}&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1548735800930'.format(
        music_name, page, pagesize)

    response = requests.get(search_url)
    print(response.text)
    response = json.loads(re.match(".*?({.*}).*", response.text, re.S).group(1))
    list = response['data']['lists']
    print(list)
    music_data = []
    for item in list:
        music_msg = ["", "", "", "暂时无法获取", ""]  # 来源、歌曲名、歌手、歌曲链接、封面图链接
        music_url = [
            'r=play/getdata',
            'callback=jQuery1910026577801017397817_1596164131720',
            'hash={}'.format(item['FileHash']),
            'album_id=',
            'dfid=0zPSYM1q2qH90xArIr1yOGtc',
            'mid=5cd316b98602d9b29f31085c96e6c682',
            'platid=4',
            '_=1596164131722'
        ]
        u = "&".join(music_url)
        response = requests.get("https://wwwapi.kugou.com/yy/index.php?" + u, headers=headers)
        html = response.text
        url = re.search('play_url":"(.*?)"', html).group(1)
        music_msg[4] = re.search('img":"(.*?)"', html).group(1).replace('\\', '')
        music_msg[3] = url.replace('\\', '')
        music_msg[0] = "酷狗"
        music_msg[1] = Drop_Em(item['OriSongName'])
        music_msg[2] = Drop_Em(item['SingerName'])
        music_data.append(music_msg)
    return music_data


if __name__ == "__main__":
    print(KugouMusic("稻香", 1, 10))
