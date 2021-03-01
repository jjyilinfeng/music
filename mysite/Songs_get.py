from mysite.Songs_Search.QQmusicSearch import QQMusic
from mysite.Songs_Search.NeteaseSearch import CloudMusic
from mysite.Songs_Search.KuwomusicSearch import KuwoMusic
from mysite.Songs_Search.KugoumusicSearch import KugouMusic

"""
一、********************************************************QQ音乐**********************************************************
1：获取歌曲mid属性值的api接口：https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=&n=&w=&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0
                                    注：参数searchid由JS源码的“Math.random()”生成并经过“replace('0.','')”等处理，参数p和n分别是页和数量，参数w是我们输入的内容
2:获取歌曲下载地址参数的api接口：https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey5165537029515912g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=
    {"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"4776407682","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"4776407682","songmid":["0039pE7x1okPVP"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}
    注：guid是固定值，跟cookie有一些关系。只有一个参数songmid，即第一个api获取到的mid
data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"4776407682","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"4776407682","songmid":["000qJ4H21yDGVW"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}
data传入时必须用json.dumps方法序列化data中的字典和列表。

二、*******************************************************网易云音乐*******************************************************
1.JS加密源码的api接口：https://s3.music.126.net/web/s/pt_frame_index_602f2359d1be3191cc19c9d1c0c170df.js?602f2359d1be3191cc19c9d1c0c170df(不需要data)
2.获取歌曲地址的api接口：https://music.163.com/weapi/cloudsearch/get/web?csrf_token=和
                      https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=(data分别为1.params，2.encSecKey。都经过了JS加密)
Js中说明4个参数来源的源码:var bUS5X=window.asrsea(JSON.stringify(i6c),bry8q(["流泪","强"]),bry8q(Sj0x.md),bry8q(["爱心","女孩","惊恐","大笑"]));e6c.data=k6e.cx7q({params:bUS5X.encText,encSecKey:bUS5X.encSecKey})
源码里window.asrsea=d，所以这四个参数对应d函数里的（d,e,f,g）：
    Sj0x.emj={"色":"00e0b","流感":"509f6","这边":"259df","弱":"8642d","嘴唇":"bc356","亲":"62901","开心":"477df","呲牙":"22677","憨笑":"ec152","猫":"b5ff6","皱眉":"8ace6","幽灵":"15bb7","蛋糕":"b7251","发怒":"52b3a","大哭":"b17a8","兔子":"76aea","星星":"8a5aa","钟情":"76d2e","牵手":"41762","公鸡":"9ec4e","爱意":"e341f","禁止":"56135","狗":"fccf6","亲亲":"95280","叉":"104e0","礼物":"312ec","晕":"bda92","呆":"557c9","生病":"38701","钻石":"14af6","拜":"c9d05","怒":"c4f7f","示爱":"0c368","汗":"5b7a4","小鸡":"6bee2","痛苦":"55932","撇嘴":"575cc","惶恐":"e10b4","口罩":"24d81","吐舌":"3cfe4","心碎":"875d3","生气":"e8204","可爱":"7b97d","鬼脸":"def52","跳舞":"741d5","男孩":"46b8e","奸笑":"289dc","猪":"6935b","圈":"3ece0","便便":"462db","外星":"0a22b","圣诞":"8e7","流泪":"01000","强":"1","爱心":"0CoJU","女孩":"m6Qyw","惊恐":"8W8ju","大笑":"d"}
    Sj0x.md=["色","流感","这边","弱","嘴唇","亲","开心","呲牙","憨笑","猫","皱眉","幽灵","蛋糕","发怒","大哭","兔子","星星","钟情","牵手","公鸡","爱意","禁止","狗","亲亲","叉","礼物","晕","呆","生病","钻石","拜","怒","示爱","汗","小鸡","痛苦","撇嘴","惶恐","口罩","吐舌","心碎","生气","可爱","鬼脸","跳舞","男孩","奸笑","猪","圈","便便","外星","圣诞"]
    i6c={"大笑":"86","可爱":"85","憨笑":"359","色":"95","亲亲":"363","惊恐":"96","流泪":"356","亲":"362","呆":"352","哀伤":"342","呲牙":"343","吐舌":"348","撇嘴":"353","怒":"361","奸笑":"341","汗":"97","痛苦":"346","惶恐":"354","生病":"350","口罩":"351","大哭":"357","晕":"355","发怒":"115","开心":"360","鬼脸":"94","皱眉":"87","流感":"358","爱心":"33","心碎":"34","钟情":"303","星星":"309","生气":"314","便便":"89","强":"13","弱":"372","拜":"14","牵手":"379","跳舞":"380","禁止":"374","这边":"262","爱意":"106","示爱":"376","嘴唇":"367","狗":"81","猫":"78","猪":"100","兔子":"459","小鸡":"450","公鸡":"461","幽灵":"116","圣诞":"411","外星":"101","钻石":"52","礼物":"107","男孩":"0","女孩":"1","蛋糕":"337",18:"186","圈":"312","叉":"313"}
    d=JSON.stringify(i6c)，e=bry8q(["流泪","强"])，f=bry8q(Sj0x.md)，g=bry8q(["爱心","女孩","惊恐","大笑"])，可以看出来，d不固定，e、f和g都是固定值
JS后四个参数至少由表情字符拼接而成（stringify有s、ids等内容的掺杂并和i6c表情集有关，bryq8在源码中定义为拼接函数），把JS化为python代码，并输出e，f，g结果：
    e='010001'
    f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g='0CoJUm6Qyw8W8jud'
d参数JS代码过于复杂，所以我选择了打断点，看后台打印出的d值，找他的规律。果然，找到了规律：
    1：接口https://music.163.com/weapi/cloudsearch/get/web?csrf_token=的d值规律：
        d={hlpretag:"<span class = "s-fc7">",hlposttag:"</span>",s:"",type:"1",csrf_token:"",total:"true",offset:"0"}
        注：其中s为歌曲名称url编码值，其他均为固定值
    2：接口https://music.163.com/weapi/song/enhance/player/url?csrf_token=的d值规律：
        d={'ids': "", 'br': 320000, 'csrf_token': ""}
        注：其中ids为歌曲的id（api一最重要的作用就是获取这个值）；br值代表音质，有两个值（320000,128000），就用最好的320000（均为mp3格式）。
        96000值(标准)的歌曲连接在另一个api中（api：https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=）这里不多说了（这个是m4a格式）。
        
三、******************************************************酷我音乐**********************************************************
1：获取歌曲rid的api接口:http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=&pn=&rn=&reqId=（key值经过url编码）
2：获取歌曲地址的api接口:http://www.kuwo.cn/url?format=mp3&rid=&response=url&type=convert_url3&br=128kmp3&from=web&t=&reqId=
                       （rid由第一个api接口获取，pn是第几页，rn是当夜歌曲数量，t为1000倍时间戳的整数部分）

四、**************************************************酷狗音乐**************************************************************
1、获取歌曲hash的api接口：https://songsearch.kugou.com/song_search_v2?callback=jQuery1124037741722730857785_%d&keyword=%s&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=%d
                        （注：共三个参数，即两个时间戳(相差2)和一个歌名的url编码。获取FileHash值）
2、获取歌曲play_url的api接口：https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery1910019528111140116433_%d&hash=%s&album_id=&dfid=%s&mid=%s&platid=4&_=%d
                             （注：共五个参数，即两个时间戳(相差1)、接口一获取到的FileHash、cookie里的kg_dfid和kg_mid）
jQuery callback是回调函数，是随机值。不带着也可以访问，但是怕服务器以此作为反爬识别措施之一，还是带上为好
"""
# 尝试获取，否则输出无法获取
init_msg = ["无法获取"]


def start(name, m_type, page, m_num):
    '''
    :param m_num: 每页的数目
    :param page: 爬取的页数
    :param m_type: 歌曲来源
    :param name: 歌曲关键字
    :return: 歌曲的详情信息：[来源、歌曲名、歌手、歌曲真实链接、歌曲封面链接]
    '''

    if 'QQ音乐' == m_type:
        return QQMusic(name, page, m_num)  # 歌曲名字、页数、目标数
    elif '网易云音乐' == m_type:
        msg = CloudMusic(name)
        return msg.sprider()
    elif '酷我音乐' == m_type:
        return KuwoMusic(name, page, m_num)  # 歌曲名字、页数、目标数
    elif '酷狗音乐' == m_type:
        return KugouMusic(name, page, m_num)  # 歌曲名字、页数、目标数


if __name__ == '__main__':
    print(start('稻香', 'QQ音乐',1,None))
