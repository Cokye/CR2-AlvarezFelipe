from django.contrib import admin
from django.urls import re_path
from .views import custom_logout

class MyAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        urls += [
            re_path(r'^logout/$', custom_logout, name='admin_logout'),
        ]
        return urls

admin_site = MyAdminSite(name='myadmin')


