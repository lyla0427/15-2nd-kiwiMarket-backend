# Generated by Django 3.1.4 on 2021-01-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210102_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
