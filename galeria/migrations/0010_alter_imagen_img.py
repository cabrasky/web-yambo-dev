# Generated by Django 4.1.1 on 2022-10-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0009_alter_imagen_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='img',
            field=models.ImageField(max_length=200, null=True, upload_to='galeria/'),
        ),
    ]
