from django.contrib import admin

from .models import *

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'language')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'page', 'item')

class GroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first', 'child')

admin.site.register(Item, ItemsAdmin)
admin.site.register(Category)
admin.site.register(Section)
admin.site.register(Tag)
admin.site.register(Language)
admin.site.register(Photo)
admin.site.register(Blog)
admin.site.register(Booking)
admin.site.register(Page)
admin.site.register(Group, GroupsAdmin)
admin.site.register(Profile, ProfileAdmin)