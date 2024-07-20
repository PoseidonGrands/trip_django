from django.db import models

# Create your models here.
class Sight(models.Model):
    name = models.CharField('景点名称', max_length=32)
    desc = models.CharField('景点描述', max_length=128, null=True, blank=True)
    content = models.TextField('景点内容')
    img = models.ImageField('图片地址', max_length=256, upload_to='%Y%m/sight')
    img_banner = models.ImageField('横幅图片地址', max_length=256, upload_to='%Y%m/sight')
    score = models.FloatField('评分', default=5)
    comment_count = models.IntegerField('评论人数', default=0)
    province = models.CharField('省份', max_length=32)
    city = models.CharField('城市', max_length=32)
    area = models.CharField('区/县', max_length=32, null=True, blank=True)
    town = models.CharField('乡镇', max_length=32, null=True, blank=True)
    min_price = models.FloatField('最低价格')
    is_hot = models.SmallIntegerField('是否热门', default=0)
    is_star = models.SmallIntegerField('是否精选', default=0)
    is_valid = models.SmallIntegerField('是否有效', default=1)
    create_at = models.DateField('创建时间', auto_now_add=True)
    update_at = models.DateField('更新时间', auto_now=True)

    class Meta:
        db_table = 'sight'
        ordering = ['-update_at']


