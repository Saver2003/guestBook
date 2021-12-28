from django.contrib import admin
from webapp.models import GuestBook

# Register your models here.

class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'status', 'created_at']
    list_filter = ['id', 'author_name', 'status', 'created_at']
    search_fields = ['author_name']
    fields = ['author_name', 'author_email', 'post_text', 'status']

admin.site.register(GuestBook, GuestBookAdmin)