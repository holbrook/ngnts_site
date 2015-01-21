from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import *

@admin.register(BizCategory)
class BizCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(BizLevel)

@admin.register(BizService)
class BizS3erviceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Application)
admin.site.register(AppService)
