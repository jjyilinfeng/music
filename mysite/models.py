from django.db import models


# 歌曲信息表song
class Music(models.Model):
    song_id = models.AutoField(db_column='id', primary_key=True)
    song_no = models.IntegerField(db_column="歌曲序号")
    song_name = models.CharField(db_column='歌名', max_length=50)
    song_singer = models.CharField(db_column='歌手', max_length=50)
    song_come = models.CharField(db_column='来源', max_length=100)
    song_link = models.CharField(db_column='音乐链接', max_length=255)
    song_img_link = models.CharField(db_column='图片链接', max_length=255)
    search_type = models.CharField(db_column='搜索类别', max_length=20)
    user_ip = models.CharField(db_column='用户IP', max_length=20)

    def __str__(self):
        return self.song_name

    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲信息'
        verbose_name_plural = '歌曲信息'


# 留言板表
class Message(models.Model):
    username = models.CharField(max_length=256)
    title = models.CharField(max_length=512)
    content = models.TextField(max_length=256)
    mail = models.CharField(max_length=100)
    publish = models.CharField(max_length=100)

    # 为了显示
    def __str__(self):
        tpl = '<Message:[username={username}, title={title}, content={content}, publish={publish}]>'
        return tpl.format(username=self.username, title=self.title, content=self.content, publish=self.publish)


# 站内搜索关键词统计
class music_key_statistics(models.Model):
    music_key = models.CharField(db_column='搜索关键词', max_length=100)
    music_key_times = models.IntegerField(db_column='搜索次数')
    user_ip = models.CharField(db_column='用户IP', max_length=20)
