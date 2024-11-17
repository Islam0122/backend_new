from django.contrib import admin
from .models import *


@admin.register(TopTales)
class TopTalesAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'created_at', 'updated_at')
    list_filter = ('user',)
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('topic',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('topic', 'text', 'user', 'created_at', 'updated_at')
        }),
    )


@admin.register(Tales)
class TalesAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'created_at', 'updated_at')
    list_filter = ('user',)
    readonly_fields = ('created_at', 'updated_at', 'user',)
    search_fields = ('topic',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('topic', 'text', 'user', 'created_at', 'updated_at')
        }),
    )

    def has_add_permission(self, request):
        return False
    #
    # def has_delete_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request):
    #     return False
