# Generated by Django 3.1.6 on 2021-06-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_Gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(default='ethio_future.jpg', upload_to=''),
        ),
    ]
