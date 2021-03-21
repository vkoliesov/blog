# Generated by Django 2.2.19 on 2021-03-21 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20210321_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlike',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='postlike',
            name='like',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], default=0, max_length=255),
        ),
        migrations.RemoveField(
            model_name='postlike',
            name='likes_user',
        ),
        migrations.AddField(
            model_name='postlike',
            name='likes_user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]