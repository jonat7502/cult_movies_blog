from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blog(models.Model):
    text = models.CharField(max_length=400)

    def __unicode__(self):
        return self.title


    def publish(self):
        self.published_date = timezone.now()
        self.save()

