from django.contrib import admin
from home.models import Contact
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','desc')
# Register your models here.
admin.site.register(Contact)