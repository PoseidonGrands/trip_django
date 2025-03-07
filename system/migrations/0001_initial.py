# Generated by Django 5.0.7 on 2024-07-20 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='图片名称')),
                ('desc', models.CharField(blank=True, max_length=32, null=True, verbose_name='描述信息')),
                ('img', models.ImageField(max_length=256, upload_to='%Y%m/slider', verbose_name='图片地址')),
                ('target_url', models.CharField(max_length=256, verbose_name='跳转地址')),
                ('types', models.IntegerField(default=10, verbose_name='展示位置')),
                ('reorder', models.IntegerField(default=0, help_text='数字越大越靠前', verbose_name='排序字段')),
                ('start_time', models.DateField(blank=True, max_length=32, null=True, verbose_name='生效开始时间')),
                ('end_time', models.DateField(blank=True, max_length=32, null=True, verbose_name='生效结束时间')),
                ('is_valid', models.SmallIntegerField(default=1, verbose_name='是否有效')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'system_slider',
                'ordering': ['-reorder'],
            },
        ),
    ]
