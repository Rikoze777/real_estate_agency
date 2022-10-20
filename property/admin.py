from django.contrib import admin
from .models import Flat, Complaint, Owner


@admin.register(Flat)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building',
                    'construction_year')
    list_editable = ['new_building']
    search_fields = ('town', 'address')
    readonly_fields = ["created_at"]
    list_filter = ['new_building']
    raw_id_fields = ["liked_by"]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]


class FlatsInline(admin.TabularInline):
    model = Flat.flat_use.through
    raw_id_fields = [
        "flat",
        "owner"
    ]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    raw_id_fields = ["flats_in_use"]
    inlines = [FlatsInline]
