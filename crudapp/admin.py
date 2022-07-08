from django.contrib import admin
from .models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','email','div','doj','marks','mob','loc']

admin.site.register(Teacher,TeacherAdmin)
