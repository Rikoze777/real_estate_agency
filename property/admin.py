from django.contrib import admin
from .models import Flat


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ["created_at"]


admin.site.register(Flat, AuthorAdmin)
