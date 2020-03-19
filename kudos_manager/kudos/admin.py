from django.contrib import admin
from .models import Kudo


class KudoAdmin(admin.ModelAdmin):
    list_display = ('id','fromColleague', 'toColleague', 'message')
    search_fields = ('message',)


admin.site.register(Kudo, KudoAdmin)
