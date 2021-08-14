# Generated by Django 3.2.5 on 2021-08-14 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(max_length=30, verbose_name='키워드')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('writer', models.CharField(max_length=30, null=True, verbose_name='작성자')),
                ('write_date', models.DateTimeField(auto_now_add=True, verbose_name='본문 생성시간')),
                ('img', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'HT_board',
            },
        ),
        migrations.CreateModel(
            name='HT_COMMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(verbose_name='댓글내용')),
                ('writer', models.CharField(max_length=30, verbose_name='댓글 작성이')),
                ('write_date', models.DateTimeField(auto_now_add=True, verbose_name='댓글 생성시간')),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeTraining.ht')),
            ],
            options={
                'db_table': 'HT_COM_board',
            },
        ),
    ]
