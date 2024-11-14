from django.contrib import admin
from django.utils.html import format_html

from .models import Group, Student


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'direction', 'group_description')
    list_filter = ('direction',)
    search_fields = ('group_name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group', 'age', 'phone_number', 'telegram',)
    list_filter = ('group',)
    search_fields = ('first_name', 'last_name', 'telegram')
    readonly_fields = ('photo_preview',)
    # fieldsets = (
    #     (None, {
    #         'fields': ('photo_preview', 'photo', 'first_name', 'last_name', 'group', 'age', 'phone_number', 'telegram',)
    #     }),)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', obj.photo.url)
        return "No photo available"

    photo_preview.short_description = "Photo Preview"
