# Generated by Django 3.2.7 on 2021-09-25 08:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likelion',
            name='like_users',
            field=models.ManyToManyField(null=True, related_name='like_counts', to=settings.AUTH_USER_MODEL, verbose_name='좋아요 수 like_users'),
        ),
    ]
