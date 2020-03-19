from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('name',)
    search_fields = ('name',)


admin.site.register(Company, CompanyAdmin)
