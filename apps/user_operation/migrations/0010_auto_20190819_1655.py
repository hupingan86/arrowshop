# Generated by Django 2.2.4 on 2019-08-19 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0009_auto_20190819_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='subject',
            new_name='title',
        ),
    ]
