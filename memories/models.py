import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class memory(models.Model):
    content = models.TextField()
    date = models.DateField(('date'), default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE())
