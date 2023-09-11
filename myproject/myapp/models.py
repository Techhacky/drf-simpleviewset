
import uuid
from django.db import models
from unixtimestampfield.fields import UnixTimeStampField
from django.utils import timezone


# Create your models here

class HomeDescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    banner_image_url = models.CharField(max_length=2000,null=True)
    heading = models.CharField(max_length=1000,null=True)
    created_at = UnixTimeStampField(use_numeric=True,default=timezone.now)

    class Meta:
        db_table = 'home_descriptions'