from django.contrib import admin
from .models import item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    search_fields = ("meal", "description")
    list_filter = ("status", )


admin.site.register(item, MenuItemAdmin)
