from django.contrib.auth.models import User
from django.db import models
from crc.widgets import *

class People(models.Model):
    name = models.CharField(max_length=50, blank=False)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='')
    title = models.CharField(max_length=20, choices=TITLE_CHOICES, default='AF')
    affiliation = models.CharField(max_length=50, blank=False)
    topics = models.ManyToManyField('Topics')
    groups = models.ManyToManyField('Groups')

    def __unicode__(self):
        return self.name

class Topics(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Papers(models.Model):
    citation = models.TextField()

    def __unicode__(self):
        return self.name

class Courses(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    professor = models.ForeignKey('People')

    def __unicode__(self):
        return self.name

class Groups(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __unicode__(self):
        return self.name