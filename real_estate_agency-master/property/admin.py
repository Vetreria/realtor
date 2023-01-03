from django.contrib import admin

from .models import Flat, Claim, Owner

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('owner','town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ( 'price', 'new_building', 'construction_year', 'town')
    list_filter = ['new_building']
    raw_id_fields = ("likes",)

    def __str__(self):
        return self.address


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['owned_flats']

 
 


admin.site.register(Flat, AuthorAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)

