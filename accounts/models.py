from django.db import models
from django.conf import settings

# Create your models here.

class TutorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    subject = models.CharField("Classes you tutor? ", max_length=150)

    mon_start = models.TimeField(null=True, blank= True)
    mon_end = models.TimeField(null=True, blank= True)

    tue_start = models.TimeField(null=True, blank= True)
    tue_end = models.TimeField(null=True, blank= True)

    wed_start = models.TimeField(null=True, blank= True)
    wed_end = models.TimeField(null=True, blank= True)

    thu_start = models.TimeField(null=True, blank= True)
    thu_end = models.TimeField(null=True, blank= True)

    fri_start = models.TimeField(null=True, blank= True)
    fri_end = models.TimeField(null=True, blank= True)
    
    description = models.TextField(blank=True, max_length=10000)

    def __str__(self):
      return f"{self.user.username} - {self.subject or 'No subject set'}"