from django.contrib import admin

# Register your models here.
from .models import Skills

class Skills_Admin(admin.ModelAdmin):
    list_display = ['left_side_skill_name','left_side_skill_percentage','right_side_skill_name','right_side_skill_percentage']

admin.site.register(Skills,Skills_Admin)  