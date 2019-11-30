from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(db_column='create_time', default=timezone.now)
    updated = models.DateTimeField(db_column='update_time', auto_now=True)
