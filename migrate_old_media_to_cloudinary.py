import os
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.apps import apps
from cloudinary.uploader import upload as cloudinary_upload
from cloudinary.utils import cloudinary_url

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SarahFoundation.settings')
import django
django.setup()

def migrate_field(model_name, field_name):
    Model = apps.get_model(*model_name.split('.'))
    for obj in Model.objects.all():
        field = getattr(obj, field_name)
        if field and not str(field).startswith('http'):  
            file_path = field.path
            print(f"Uploading {file_path} ...")
            result = cloudinary_upload(file_path, folder=f"{model_name}/{field_name}")
            if result.get("secure_url"):
                
                uploaded_file = SimpleUploadedFile(
                    name=os.path.basename(file_path),
                    content=open(file_path, "rb").read()
                )
                setattr(obj, field_name, uploaded_file)
                obj.save()
                print(f"Uploaded {file_path}")
            else:
                print(f"Failed: {file_path}")


migrate_field("Events.Event", "image")
