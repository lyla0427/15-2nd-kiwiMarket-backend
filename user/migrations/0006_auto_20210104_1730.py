# Generated by Django 3.1.4 on 2021-01-04 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210104_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='district',
            new_name='dong',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='neighborhood',
            new_name='sido',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='region',
            new_name='sigungu',
        ),
    ]
