from __future__ import absolute_import

import os
from celery import Celery

# 设置运行时的环境变量
from ContentMS import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ContentMS.settings")

# 创建Celery的应用, 类似于Flask
capp = Celery(__name__)

# 配置celery应用环境,扩展：APScheduler (Flask)
capp.config_from_object('django.conf:settings')

# 自动查找task标记 @capp.task 装饰函数
capp.autodiscover_tasks(lambda : settings.INSTALLED_APPS)