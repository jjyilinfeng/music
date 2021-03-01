# 导入爬虫文件
from mysite.Url_Spiders.NeteaseSpiders import NeteaseSpider
from mysite.Url_Spiders.KuwoSpiders import KuwoSpider
from mysite.Url_Spiders.KogouSpiders import KugouSpider
from mysite.Url_Spiders.QQmusicSpiders import QQMusicSpider
from mysite.Url_Spiders.LizhiFMSpiders import LizhifmSpider
from mysite.Url_Spiders.QianqianSpiders import Qianqianspider
from mysite.Url_Spiders.FivesingSpiders import FivesingSpider


def main(url):
    """
    :param url: 歌曲的链接url
    :return: 歌曲的详情信息:歌曲真实地址url、歌曲名字、歌手、专辑名、歌词、专辑图片地址
    """
    # 歌曲下载信息初始
    Download_Msg = {
        'music_url': "",
        'music_name': "",
        'music_singer': "",
        'music_album': "",
        'music_lyric': "",
        'music_image_url': ""}

    # 歌曲下载默认信息
    Init_Msg = {
        'music_url': "下载地址会显示在这儿哦，如果没显示就是获取失败了",
        'music_name': "当前歌曲不支持获取",
        'music_singer': "当前歌曲不支持获取",
        'music_album': "当前歌曲不支持获取",
        'music_lyric': "当前歌曲不支持获取",
        'music_image_url': "当前歌曲不支持获取"
    }

    # 清空歌词文件
    lyric_file = open("lyric.lrc", "w+")
    lyric_file.write("")
    lyric_file.close()

    # 判断网址来源，并执行相应的函数
    if "https://music.163.com" in url:
        # 例子：https://music.163.com/#/song?id=1343016814
        Download_Msg = NeteaseSpider(url)

    elif "https://www.kugou.com/song/#hash=" and "&album_id" in url:
        # 例子：https://www.kugou.com/song/#hash=C543BD2D1CC2C47A1F605404D608CD89&album_id=36026299
        spider = KugouSpider(url)
        Download_Msg = spider.get_music_playurl()

    elif "http://www.kuwo.cn/play_detail/" in url:
        # 例子：http://www.kuwo.cn/play_detail/64157401
        Download_Msg = KuwoSpider(url)

    elif 'https://y.qq.com/n/yqq/song/' in url:
        # 例子：https://y.qq.com/n/yqq/song/001uJfwA2yjOUm.html
        spider = QQMusicSpider(url)
        Download_Msg = spider.music_msg_spider()

    elif 'https://www.lizhi.fm/' in url:
        Download_Msg = LizhifmSpider(url)
        # 例子：https://www.lizhi.fm/1244717/5112178580883627142

    elif 'http://music.taihe.com/song/' in url:
        # 例子：http://music.taihe.com/song/23328945
        Download_Msg = Qianqianspider(url)

    elif 'http://5sing.kugou.com/' in url:
        # 例子：http://5sing.kugou.com/yc/4183524.html
        Download_Msg = FivesingSpider(url)

    # 为空值添加默认值
    for k in Download_Msg.keys():
        if not Download_Msg[k]:
            Download_Msg[k] = Init_Msg[k]

    return Download_Msg


if __name__ == "__main__":
    print(main("https://www.lizhi.fm/551550/5126699846247448582"))
