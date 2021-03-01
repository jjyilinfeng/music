import requests


def KuwoMusic(music_name, page, page_items):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
        'csrf': 'RUJ53PGJ4ZD',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD'
    }

    singer = music_name
    url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn={}&httpsStatus=1&reqId=98d1a930-d789-11ea-a745-f73ea03e3468".format(
        singer, page, page_items)
    response = requests.get(url, headers=headers).json()

    data = response['data']['list']
    print(data)
    data_music = []
    for x in data:
        music_msg = ["", "", "", "", ""]  # 来源、歌曲名、歌手、歌曲链接、专辑名
        rid = x["rid"]
        try:
            music_url = "http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1582894271662&reqId=ff4d2920-5a28-11ea-a40f-c96cc7a8aad1".format(
                rid)
            music_msg[0] = "酷我"
            music_msg[3] = requests.get(music_url, headers=headers).json()['url']
            music_msg[1] = x['name']
            music_msg[2] = x['artist']
            if 'pic' in x:
                music_msg[4] = x['pic']
        except Exception:
            print(Exception)
        data_music.append(music_msg)
    return data_music


if __name__ == "__main__":
    data = KuwoMusic("Env", 1, 10)
    for i in data:
        print(i)
