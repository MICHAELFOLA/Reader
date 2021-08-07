from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    Content_Type = models.CharField(max_length=255)
    Article_Title = models.CharField(max_length=255)
    Words_Per_Column = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'search done on {self.header} at {self.created}'

     