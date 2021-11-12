from django.contrib import admin
from .models import Room, Message

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user', 'room')

admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)