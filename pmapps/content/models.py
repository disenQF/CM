import uuid

import os
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='名称')

    add_time = models.DateTimeField(verbose_name='添加时间',
                                    auto_now_add=True)

    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               verbose_name='所属分类',
                               blank=True,
                               null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    code = models.CharField(max_length=10, verbose_name='编号')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['code']  # 排序字段


class Book(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='名称')

    author = models.CharField(max_length=50,
                              verbose_name='作者')

    summary = models.CharField(max_length=100,
                               verbose_name='概要',
                               null=True)

    info = models.TextField(verbose_name='作品信息',
                            null=True)

    cover = models.ImageField(verbose_name='封面',
                              null=True,
                              blank=True,
                              width_field='cover_width',
                              height_field='cover_height',
                              upload_to='book/images/')  # 相对于 MEDIA_ROOT的子目录

    cover_width = models.IntegerField(verbose_name='宽度',
                                      null=True, default=0, blank=True)
    cover_height = models.IntegerField(verbose_name='高度',
                                       null=True,default=0, blank=True)

    # 多对多的关系, 自动创建第三方表
    tags = models.ManyToManyField(Tag,
                                  verbose_name='标签')

    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='所属分类')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if len(self.cover.name) < 32:
            uuid_str = str(uuid.uuid4()).replace('-', '')
            self.cover.name = uuid_str + os.path.splitext(self.cover.name)[-1]

        super().save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_book'
        verbose_name = '小说'
        verbose_name_plural = verbose_name
