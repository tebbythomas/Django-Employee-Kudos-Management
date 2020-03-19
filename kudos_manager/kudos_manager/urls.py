from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    # Home page / Dashboard is router to pages.urls
    path('', include('pages.urls')),
    # Account login, logout and register are routed here
    path('accounts/', include('accounts.urls')),
    # Admin section
    path('admin/', admin.site.urls),
]
