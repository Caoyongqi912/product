# Generated by Django 2.0.6 on 2019-07-03 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论人'),
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='文章作者'),
        ),
        migrations.AddField(
            model_name='articles',
            name='classify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.Classify', verbose_name='文章类别'),
        ),
    ]
