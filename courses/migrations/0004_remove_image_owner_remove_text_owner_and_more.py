# Generated by Django 4.0.4 on 2022-05-20 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_remove_content_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='text',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='video',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='content',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='content',
            name='object_id',
        ),
        migrations.AddField(
            model_name='content',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='content_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='video',
            field=models.FileField(default=1, upload_to='courses/video/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
