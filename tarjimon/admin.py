from django.contrib import admin
from .models import Lugat

class LugatAdmin(admin.ModelAdmin):

    list_display = ['inglizcha', 'uzbekcha']

admin.site.register(Lugat, LugatAdmin)
