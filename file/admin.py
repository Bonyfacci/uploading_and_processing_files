from django.contrib import admin

from file.models import File


@admin.register(File)
class FileListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'file', 'uploaded_at', 'processed')
    search_fields = ('name',)
