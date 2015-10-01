from django.contrib import admin

from .models import Message

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['message_text', 'name_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('message_text', 'pub_date', 'name_text')

admin.site.register(Message, MessageAdmin)