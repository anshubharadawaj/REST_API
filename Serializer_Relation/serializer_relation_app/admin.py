from django.contrib import admin

# Register your models here.
from .models import Singer,Song
# from .models import Student

admin.site.register(Singer)
admin.site.register(Song)
# admin.site.register(Student)