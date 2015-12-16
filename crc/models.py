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

class Topics(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

class Papers(models.Model):
    citation = models.TextField()

class Courses(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    professor = models.ForeignKey('People')

class Groups(model.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()