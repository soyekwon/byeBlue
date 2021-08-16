from django.db import models
from django.core.validators import validate_email

class User(models.Model):
    name = models.CharField(max_length=30, unique = True, verbose_name="닉네임")
    email = models.EmailField(max_length = 30, unique=True, validators=[validate_email], verbose_name="이메일")
    pw = models.CharField(max_length = 20, verbose_name="비밀번호")
    joindate = models.DateTimeField(auto_now_add= True, verbose_name="계정 생성시간")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'