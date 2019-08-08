# Generated by Django 2.2.4 on 2019-08-08 11:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=20, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别code', max_length=20, verbose_name='类别code')),
                ('desc', models.TextField(default='', help_text='类别描述', max_length=200, verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
            },
        ),
    ]
