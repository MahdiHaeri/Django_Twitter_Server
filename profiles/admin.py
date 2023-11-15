from django.contrib import admin

from profiles.models import Bio


# Register your models here.

class BioAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'biography', 'location', 'website', 'created_at', 'updated_at')


admin.site.register(Bio, BioAdmin)
