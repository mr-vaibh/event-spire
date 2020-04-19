from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Centre, Event

# Register your models here.

admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'Events'

class CentreAdmin(admin.ModelAdmin):
    list_display = ['id', 'centre_name', 'date_time']
    list_filter = ['date_time']

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_img', 'centre', 'date_time']
    list_filter = ['date_time']

admin.site.unregister(Group)
admin.site.register(Centre, CentreAdmin)
admin.site.register(Event, EventAdmin)