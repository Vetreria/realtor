from django.contrib import admin

from .models import Flat, Claim, Owner


class OwnerFlatInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ("owner", "flat")


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ( 'price', 'new_building', 'construction_year', 'town')
    list_filter = ['new_building']
    raw_id_fields = ("likes",)
    inlines = [
        OwnerFlatInline,
    ]

    def __str__(self):
        return self.address

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']

 
 





