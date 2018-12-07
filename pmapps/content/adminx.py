import xadmin as admin
from xadmin import views

from content.models import Category, Book, Tag


# Register your models here.


class BaseSetting(object):
    # 主题修改
    enable_themes = False
    use_bootswatch = False


admin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    # 整体配置
    site_title = '内容后台管理系统'
    site_footer = '千锋教育python项目'
    menu_style = 'accordion'  # 菜单折叠
    # 搜索模型
    global_search_models = [Category, Book]

    # 模型的图标(参考bootstrap图标插件)
    global_models_icon = {
        Book: "glyphicon glyphicon-book",
        Category: "fa fa-cloud"
    }  # 设置models的全局图标

    # 设置app模块的标题
    apps_label_title = {
        'content': '内容管理',
        'order': '订单管理'
    }

    # 设置app模块的图标
    apps_icons = {
        'content': 'glyphicon glyphicon-book',
        'order': 'glyphicon glyphicon-barcode'
    }


admin.site.register(views.CommAdminView, GlobalSettings)


class CategoryAdmin:
    # 后台列表显示列
    list_display = ['name', 'add_time', 'parent']

    # 后台列表查询条件
    search_fields = ['name']

    # 后台列表通过时间查询
    list_filter = ['name']

    list_per_page = 20


class BookAdmin:
    # 后台列表显示列
    list_display = ['name', 'summary', 'author', 'category', 'tags']
    # 后台列表查询条件
    search_fields = ['name', 'author']
    list_per_page = 20


class TagAdmin:
    # 后台列表显示列
    list_display = ['name', 'code']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Tag, TagAdmin)
