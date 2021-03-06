# Generated by Django 3.2.8 on 2022-03-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backcall',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Электронный адресс'),
        ),
        migrations.AddField(
            model_name='backcall',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос или пожeлание'),
        ),
        migrations.AddField(
            model_name='backcall',
            name='theme',
            field=models.TextField(blank=True, null=True, verbose_name='Тема'),
        ),
    ]
