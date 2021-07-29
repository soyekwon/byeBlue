# Generated by Django 3.2.5 on 2021-07-29 14:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='닉네임')),
                ('email', models.EmailField(max_length=30, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='이메일')),
                ('pw', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('joindate', models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]