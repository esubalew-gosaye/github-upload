# Generated by Django 3.1.6 on 2021-06-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_Gallery', '0003_auto_20210605_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.TextField(max_length=30),
        ),
    ]
