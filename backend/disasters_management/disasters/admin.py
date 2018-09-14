from django.contrib import admin

# Register your models here.
from .models import Disaster


class DisasterAdmin(admin.ModelAdmin):
    exclude = ('center_point',)


    def author_first_name(self, obj):
        return obj.title



admin.site.register(Disaster, DisasterAdmin)