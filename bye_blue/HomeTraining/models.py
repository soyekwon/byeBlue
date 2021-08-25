from django.db import models
from account.models import User


class HT(models.Model):
    part = models.CharField(max_length=30, verbose_name="키워드")
    title = models.CharField(max_length=30, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.CharField(max_length=30, verbose_name="작성자", null=True)
    write_date = models.DateTimeField(auto_now_add=True, verbose_name="본문 생성시간")
    images = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "HT_board"


class HT_COMMENT(models.Model):
    board = models.ForeignKey(HT, on_delete=models.CASCADE, null=True)
    contents = models.TextField(verbose_name="댓글내용")
    writer = models.CharField(max_length=30, verbose_name="댓글 작성이")
    write_date = models.DateTimeField(auto_now_add=True, verbose_name="댓글 생성시간")

    def __str__(self):
        return self.writer

    class Meta:
        db_table = "HT_COM_board"


class YoutubeHt(models.Model):
    youtube_title = models.CharField(max_length=100, verbose_name="유튜브제목", unique=True)
    youtube_url = models.CharField(max_length=100, verbose_name="링크")
    youtube_view = models.CharField(max_length=100, verbose_name="클릭수")

    def __str__(self):
        return str(self.youtube_title)

    class Meta:
        db_table = "HT_youtube"
