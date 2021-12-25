# Generated by Django 3.1.6 on 2021-06-05 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_Gallery', '0002_gallery_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Photo_Gallery.category'),
        ),
    ]
