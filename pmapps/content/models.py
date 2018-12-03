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

class Book(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='名称')

    author = models.CharField(max_length=50,
                            verbose_name='作者')

    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='所属分类')

    def __str__(self):
        return self.name

