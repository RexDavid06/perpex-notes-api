from django.contrib import admin
from .models import Note

# Register your models here.

class CustomeAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "owner")
    search_fields = ("title", "content")
    readonly_fields = ['owner']


admin.site.register(Note, CustomeAdmin)