# Generated by Django 4.1.1 on 2022-09-26 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitores', '0003_grupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='monis',
        ),
        migrations.AddField(
            model_name='monitor',
            name='grupos',
            field=models.ManyToManyField(to='monitores.grupo'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='img',
            field=models.ImageField(max_length=200, null=True, upload_to='fotos_monitores/'),
        ),
    ]
