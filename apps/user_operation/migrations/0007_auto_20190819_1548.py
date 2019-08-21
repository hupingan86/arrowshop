# Generated by Django 2.2.4 on 2019-08-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0006_auto_20190819_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='message_type',
            field=models.IntegerField(choices=[(1, '留言'), (2, '投诉'), (3, '询问'), (4, '售后'), (5, '求购')], default=1, help_text='留言类型:1(留言),2(投诉),3(询问),4(售后),5(求购)', verbose_name='留言类型'),
        ),
    ]
