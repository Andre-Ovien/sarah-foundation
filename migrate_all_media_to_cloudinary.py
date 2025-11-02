import os
import django
from cloudinary.uploader import upload as cloudinary_upload
from django.core.files.storage import default_storage
from django.apps import apps

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SarahFoundation.settings")
django.setup()

MEDIA_ROOT = os.path.join(os.getcwd(), "media")

def upload_file_to_cloudinary(file_path, folder):
    print(f"Uploading {file_path} ...")
    result = cloudinary_upload(file_path, folder=folder)
    print(f"✅ Uploaded: {result.get('secure_url')}")
    return result.get("secure_url")

def migrate_model_field(model_name, field_name):
    model = apps.get_model(model_name)
    objs = model.objects.all()

    for obj in objs:
        file_field = getattr(obj, field_name, None)
        if not file_field:
            continue
        local_path = file_field.path if hasattr(file_field, "path") else None
        if local_path and os.path.exists(local_path):
            new_url = upload_file_to_cloudinary(local_path, f"{model_name}/{field_name}")
            file_field.name = new_url
            obj.save(update_fields=[field_name])
        else:
            print(f"⚠️ Skipped: {obj} (no local file found)")

def upload_all_media():
    print("\n🚀 Starting full media upload migration...\n")
    for root, dirs, files in os.walk(MEDIA_ROOT):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_path, MEDIA_ROOT)
            folder = os.path.dirname(relative_path)
            upload_file_to_cloudinary(file_path, folder)
    print("\n✅ All media files uploaded successfully.\n")

if __name__ == "__main__":
    # STEP 1: Upload all local media files
    upload_all_media()

    # STEP 2: Optionally, sync with your models (example: Events and Blogs)
    migrate_model_field("Events.Event", "image")
    migrate_model_field("Blog.BlogPost", "image")

    print("\n🎯 Migration complete. All files should now exist in Cloudinary.\n")
