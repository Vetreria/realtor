from django.contrib import admin

from .models import Flat

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('owner','town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ( 'price', 'new_building', 'construction_year', 'town')

    def __str__(self):
        return self.address
 
 


admin.site.register(Flat, AuthorAdmin)
