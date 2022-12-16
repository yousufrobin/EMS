from django.contrib import admin

from app_EMS.models import Department, Employee, Role

# Register your models here.
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Employee)
