# Generated by Django 2.1 on 2018-09-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ostacor', '0021_auto_20180913_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createstory_media',
            name='image_file',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='createstory_media',
            name='text_desc',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]