# Generated by Django 4.1.1 on 2022-10-03 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_post_postimage_remove_monitor_grupos_delete_grupo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
