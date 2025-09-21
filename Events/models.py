from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    description = models.TextField()
    start_time = models.TimeField(default="12:00:00")
    end_time = models.TimeField(default="12:00:00")
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    highlight_1 = models.TextField(blank=False)
    highlight_2 = models.TextField(blank=False)
    highlight_3 = models.TextField(blank=False)
    highlight_4 = models.TextField(blank=False)
    highlight_5 = models.TextField(blank=False)
    image_1 = models.ImageField(upload_to="Events_gallery")
    image_2 = models.ImageField(upload_to="Events_gallery") 
    image_3 = models.ImageField(upload_to="Events_gallery")

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