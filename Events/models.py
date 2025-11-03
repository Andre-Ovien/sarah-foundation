from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Event(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    description = models.TextField()
    start_time = models.TimeField(default="12:00:00")
    end_time = models.TimeField(default="12:00:00")
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(storage=MediaCloudinaryStorage(),upload_to='events/', blank=True, null=True, max_length=500)
    is_live = models.BooleanField(default=True)

    highlight_1 = models.TextField(blank=False)
    highlight_2 = models.TextField(blank=False)
    highlight_3 = models.TextField(blank=False)
    highlight_4 = models.TextField(blank=False)
    highlight_5 = models.TextField(blank=False)
    image_1 = models.ImageField(storage=MediaCloudinaryStorage(),upload_to="Events_gallery",blank=True, null=True, max_length=500)
    image_2 = models.ImageField(storage=MediaCloudinaryStorage(),upload_to="Events_gallery",blank=True, null=True, max_length=500) 
    image_3 = models.ImageField(storage=MediaCloudinaryStorage(),upload_to="Events_gallery",blank=True, null=True, max_length=500)

    def __str__(self):
        return self.title
    

class RegisterEvent(models.Model):
    class StatusChoices(models.TextChoices):
        TEENAGER = 'TEENAGER'
        ADULT = 'ADULT'

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=False)
    status = models.CharField(
        max_length=20,
        choices = StatusChoices.choices,
        default= StatusChoices.TEENAGER
    )

    def __str__(self):
        return f"{self.full_name}-{self.event.title}"