from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

class EmployeeAdmin(SimpleHistoryAdmin):
    list_display = ['first_name', 'last_name', 'department']
    list_filter = ['department']

class DepartmentAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,DepartmentAdmin)


