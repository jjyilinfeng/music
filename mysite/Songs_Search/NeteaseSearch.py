import requests, execjs, codecs, json


class CloudMusic():
    def __init__(self, name):
        self.name = name
        self.e = '010001'
        self.f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7 '
        self.g = '0CoJUm6Qyw8W8jud'
        self.init_music_msg = [["网易云", "什么都没有找到", "可能是因为没有版权", "嘤嘤嘤", ""]]

    def get_data(self, d):
        self.d = d
        with open('E:\python\project\music\static\js\cloud.js', encoding='utf-8')as f:
            JS = f.read()
        data_ = execjs.compile(JS).call('d', self.d, self.g)
        self.i = data_['A'][::-1]
        data = {
            'params': data_['encText'],
            'encSecKey': format(
                int(codecs.encode(self.i.encode('utf-8'), 'hex_codec'), 16) ** int(self.e, 16) % int(self.f, 16),
                'x').zfill(256)
        }
        return data

    def get_id(self):
        url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        headers = {
            'Referer': 'https://music.163.com/search/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        d = '{hlpretag:"<span class = \'s-fc7\'>",hlposttag:"</span>",s:"%s",type:"1",csrf_token:"",total:"true",offset:"0"}' % self.name
        # print(self.get_data(d))
        response = \
        json.loads(requests.post(url=url, headers=headers, data=self.get_data(d)).content.decode('utf-8'))['result'][
            'songs']
        print(response)
        return [x['id'] for x in response], list(
            map(lambda x: ['网易云', x['name'], '/'.join([i['name'] for i in x['ar']])], response))

    def sprider(self):
        try:
            IDs, informations = self.get_id()
            for ID, information in zip(IDs, informations):
                information.append("http://music.163.com/song/media/outer/url?id=" + str(ID))
                information.append(
                    "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596979727670&di=2e3c21052e18174e372720c56e662331&imgtype=0&src=http%3A%2F%2Fwww.zyqhwj.com%2Fuploads%2Fallimg%2F190221%2F1545419604_0.jpg")
            return informations
        except Exception:
            return self.init_music_msg


if __name__ == "__main__":
    msg = CloudMusic('稻香')
    print(msg.sprider())
