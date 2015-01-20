from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import *

@admin.register(BizCategory)
class BizCategoryAdmin(MPTTModelAdmin):
    pass

@admin.register(BizService)
class BizS3erviceAdmin(admin.ModelAdmin):
    pass
