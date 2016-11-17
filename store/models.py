from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


    def publish(self):
        self.published_date = timezone.now()
        self.save()
