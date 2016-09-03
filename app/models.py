# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from tagging.fields import TagField
from markdown import markdown
from django.db.models import permalink
from django.conf import settings
from django.db.models import permalink
from django.conf import settings

# Create your models here.
class Category(models.Model):
	title=models.CharField(max_length=100, unique=True)
	slug=models.SlugField(max_length=100, unique=True)
	description=models.CharField(max_length=500)
	class Meta:
		ordering=['title']
		verbose_name_plural = "Categories"
	def __unicode__(self):
		return  "/category/%s/" % self.title
	def get_absolute_url(self):
		return self.slug

class Event(models.Model):
	LIVE_STATUS=1
	DRAFT_STATUS=2
	HIDDEN_STATUS=3
	LEISURE_EVENT=1
	CULTURAL_EVENT=2
	BALLS=3
	AWARDS_AND_GALLAS=4
	STATUS_CHOICES = ( (LIVE_STATUS, 'Live'),(DRAFT_STATUS, 'Draft'), (HIDDEN_STATUS, 'Hidden'))
	CATEGORY_CHOICES = ((LEISURE_EVENT, 'leisure'),(CULTURAL_EVENT, 'cultural'), (BALLS, 'balls'), (AWARDS_AND_GALLAS,'awards_and_gallas'))
	title=models.CharField(max_length=100, unique=False)
	description=models.TextField(blank=False)
	location=models.TextField(max_length=100, unique=False)
	inattendance=TagField()
	event_date=models.DateField(blank=False)
	regular_ticket_price=models.IntegerField(max_length=100, unique=False)
	vip_ticket_price=models.IntegerField(max_length=100, unique=False)
	vvip_ticket_price=models.IntegerField(max_length=100, unique=False)
	slug=models.SlugField(max_length=100, blank=False)
	post_date=models.DateField(default=datetime.now, blank=False)
	author=models.ForeignKey(User)
	enable_comments=models.BooleanField(default=True)
	featured=models.BooleanField(default=False)
	status = models.IntegerField(choices = STATUS_CHOICES, default = LIVE_STATUS)
	category=models.IntegerField(choices=CATEGORY_CHOICES, default=LEISURE_EVENT)
	image=models.ImageField(upload_to='images', blank=False)

	class Meta:
		ordering=['-post_date']
		verbose_name_plural="Events"
	def __unicode__(self):
		return '%s' %self.title
	def get_absolute_url(self):
		return(self.slug)


class newsletter(models.Model):
	email=models.CharField(max_length=200, unique=True)
	date=models.DateField(default=datetime.now, blank=False)

	class Meta:
		ordering=['-date']
	def __unicode__(self):
		return self.email




