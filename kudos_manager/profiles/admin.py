from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company', 'kudosCount', 'kudosLastUpdated')
    list_filter = ('user', 'company', 'kudosCount', 'kudosLastUpdated')
    list_editable = ('user', 'company', 'kudosCount')
    search_fields = ('user', 'company', 'kudosCount', 'kudosLastUpdated')


admin.site.register(Profile, ProfileAdmin)
