from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from account.models import *

class Online(models.Model):
    writer = models.ForeignKey(User, on_delete=CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    pub_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]




