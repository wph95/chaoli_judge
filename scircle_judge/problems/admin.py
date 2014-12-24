from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import User
from models import Problem

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'level', 'author',)
    list_filter = ('level', 'status')
    filter_horizontal = ('tags', )
    search_fields = ('name', )
    raw_id_fields = ('author', )
        
admin.site.register(Problem, ProblemAdmin)        