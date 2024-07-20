from django.db import models


class Slider(models.Model):
    name = models.CharField('图片名称', max_length=32)
    desc = models.CharField('描述信息', max_length=32, null=True, blank=True)
    img = models.ImageField('图片地址', max_length=256, upload_to='%Y%m/slider')
    target_url = models.CharField('跳转地址', max_length=256)
    types = models.IntegerField('展示位置', default=10)
    reorder = models.IntegerField('排序字段', default=0, help_text='数字越大越靠前')
    start_time = models.DateField('生效开始时间', max_length=32, null=True, blank=True)
    end_time = models.DateField('生效结束时间', max_length=32, null=True, blank=True)
    is_valid = models.SmallIntegerField('是否有效', default=1)
    create_at = models.DateField('创建时间', auto_now_add=True)
    update_at = models.DateField('更新时间', auto_now=True)

    class Meta:
        db_table = 'system_slider'
        ordering = ['-reorder']

