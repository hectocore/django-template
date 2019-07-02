from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User


# Admin models
class UserAdmin(DjangoUserAdmin):
    add_fieldsets = DjangoUserAdmin.add_fieldsets
    add_fieldsets[0][1]["fields"] = add_fieldsets[0][1]["fields"][:1] + ("email",) + add_fieldsets[0][1]["fields"][1:]


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.site_header = '{{cookiecutter.project_name}} Admin'
