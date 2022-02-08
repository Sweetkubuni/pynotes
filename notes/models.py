from django.db import models
from django.utils import timezone

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length = 100, default='Title To Be Changed')
    body = models.CharField(max_length = 100, default='Body needs Update!')
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True, default=timezone.now)
    last_modified =  AutoDateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
