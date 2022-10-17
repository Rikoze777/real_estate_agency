from django.contrib import admin
from .models import Flat, Complaint


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ["created_at"]
    list_filter = ['new_building']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]


admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ComplaintAdmin)
