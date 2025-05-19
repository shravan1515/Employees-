from django.contrib import admin
from .models import Employee, Role, Department
# Register your models here.

class showDepartment(admin.ModelAdmin):
    list_display = ["id", "name", "location"]

admin.site.register(Department, showDepartment)

class showRole(admin.ModelAdmin):
    list_display = ["id", "name"]
admin.site.register(Role, showRole)

class showEmployee(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "dept", "salary", "bonus", "role", "phone", "location", "hire_date"]

admin.site.register(Employee, showEmployee)



