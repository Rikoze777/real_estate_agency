from django.contrib import admin
from .models import Flat, Complaint, Owner


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building',
                    'construction_year')
    list_editable = ['new_building']
    search_fields = ('town', 'address')
    readonly_fields = ["created_at"]
    list_filter = ['new_building']
    raw_id_fields = ["liked_by"]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner',)
    raw_id_fields = ["flats_in_use"]


admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
