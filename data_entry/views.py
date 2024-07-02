from django.shortcuts import render, redirect
from .utils import get_all_custom_models
from data_uploads.models import Upload
from automation_everything import settings
from django.core.management import call_command


def import_data(request):
    if request.method == "POST":
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        relative_path = str(upload.file.url)
        base_path = str(settings.BASE_DIR)
        file_path = base_path + relative_path
        call_command('importdatamodel', file_path, model_name)
        return render(request, "data_entry/import-data.html")
    else:
        all_models = get_all_custom_models()
        context = {
            "all_models":all_models
        }
        return render(request, "data_entry/import-data.html", context=context)