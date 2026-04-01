from django.contrib import admin

from .models import Note

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'pub_date', 'is_public']


admin.site.register(Note, NoteAdmin)