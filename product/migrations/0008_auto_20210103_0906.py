# Generated by Django 3.1.4 on 2021-01-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210103_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image_url',
            field=models.URLField(max_length=2000, null=True),
        ),
    ]