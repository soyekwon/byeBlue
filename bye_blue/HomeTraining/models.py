from django.db import models
from account.models import User

class HT(models.Model):
    part = models.CharField(max_length=30, verbose_name="키워드")
    title = models.CharField(max_length = 30,verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.CharField(max_length=30, verbose_name="작성자",null=True)
    write_date = models.DateTimeField(auto_now_add= True, verbose_name="본문 생성시간")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'HT_board'
