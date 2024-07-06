from django.contrib import admin
from .models import student
# Register your models here.
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'dob', 'reg','test']