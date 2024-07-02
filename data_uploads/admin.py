from django.contrib import admin
from .models import Upload


class UploadModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'file', 'uploaded_at')


admin.site.register(Upload, UploadModelAdmin)