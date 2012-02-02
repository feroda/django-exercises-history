from django.db import models

from djex_history.history.models import HistoricalRecords

class Book(models.Model):

    title = models.CharField(max_length=256)

    history = HistoricalRecords()

    def __unicode__(self):
        return self.title

class Author(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    book = models.ForeignKey(Book)

    history = HistoricalRecords()

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
