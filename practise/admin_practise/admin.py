from django.contrib import admin

from .models import *

@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
 fieldsets = ((None, {'fields': ('firstname', 'lastname')}),('Advanced options', {'classes': ('collapse',),
            'fields': ('registration_required', 'template_name'),
        }),
    )