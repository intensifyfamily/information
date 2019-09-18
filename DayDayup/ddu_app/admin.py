from django.contrib import admin
from .models import StudentsInfo

# admin.site.site_header = '修改后'
# admin.site.site_title = '哈哈'
# Blog模型的管理器
@admin.register(StudentsInfo)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_name', 'stu_num', 'stu_age', 'sex', 'stu_birth', 'phone', 'college', 'class_num', 'major', 'depart', 'position', 'stu_id', 'nation', 'stu_addr', 'others')

    ordering = ('depart', 'sex')
    list_display_links = ('stu_name', 'stu_num')
    # 筛选器
    list_filter = ('college', 'depart')  # 过滤器
    search_fields = ('stu_num', 'stu_name', 'depart')  # 搜索字段
