from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student_Data)

class Student_data_admin(admin.ModelAdmin):
    pass
