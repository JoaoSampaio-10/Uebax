from django.contrib import admin
from .models import ClickEvent

@admin.register(ClickEvent)
class ClickEventAdmin(admin.ModelAdmin):
    list_display = ('user', 'element_name', 'timestamp')
    list_filter = ('user', 'element_name')
    ordering = ('-timestamp',)
