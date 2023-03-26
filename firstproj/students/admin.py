from django.contrib import admin
from students.models import student
# Register your models here.
class studentAdmin(admin.ModelAdmin):
	list_display = ("stdName", "stdID", "stdSex")
	list_filter = ("stdSex",)
	search_fields=('stdName', "stdID")
admin.site.register(student, studentAdmin)