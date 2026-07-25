from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Circle(models.Model):
    name = models.CharField(max_length=50)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_circles', default=None)
    code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name