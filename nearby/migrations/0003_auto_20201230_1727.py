# Generated by Django 3.1.4 on 2020-12-30 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nearby', '0002_auto_20201230_0704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nearby',
            old_name='comment_id',
            new_name='comment',
        ),
    ]