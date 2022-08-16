from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Inquiry)
class InquiryAdmin(admin.ModelAdmin):
   list_display = ('name', 'subject', 'inqury_date')
   list_display_links = ('name', 'inqury_date')
   list_filter = ('inqury_date',)
   search_fields = ('name', 'email', 'subject', 'message')
   ordering = ('-inqury_date',)    

@admin.register(models.OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
   list_display = ('name', 'position')

@admin.register(models.ContactUsDetails)
class ContactUsAdmin(admin.ModelAdmin):
   pass

@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
   list_display = ('email', 'subscribed_at')      
   search_fields = ('email',)
   ordering = ('-subscribed_at',)
   date_hierarchy = 'subscribed_at'   