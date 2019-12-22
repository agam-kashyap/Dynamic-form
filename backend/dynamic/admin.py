from django.contrib import admin

# Register your models here.
from dynamic.models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','members')

admin.site.register(Team,TeamAdmin)