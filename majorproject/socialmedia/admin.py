from django.contrib import admin

from socialmedia.models import Library,Register,Loginn,admin_login,adminlogin

# Register your models here.
admin.site.register(Library),
admin.site.register(Register),
admin.site.register(Loginn),
admin.site.register(admin_login),
admin.site.register(adminlogin),
