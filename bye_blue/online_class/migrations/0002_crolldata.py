# Generated by Django 3.2.5 on 2021-08-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrollData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
    ]
