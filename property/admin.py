from django.contrib import admin

from .models import Flat, Claim, Owner


class OwnerFlatInline(admin.TabularInline):
    model = Owner.owned_flats.through
    raw_id_fields = ("owner", "flat")


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner','town', 'address',)
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


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['owned_flats']

 
 


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)

