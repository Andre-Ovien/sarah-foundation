from django.contrib import admin
from .models import Event, RegisterEvent

# Register your models here.

admin.site.register(Event)
admin.site.register(RegisterEvent)