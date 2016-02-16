from __future__ import unicode_literals

from django.db import models

class Listing(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	OTHER = 'Other'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		(OTHER, 'Other'),
		)
	gender_choices = models.CharField(max_length=5, choices=GENDER_CHOICES, default=MALE)

	SHARED = 'Shared'
	PRIVATE = 'Private'
	MARRIED = 'Married'
	ROOM_TYPE = (
		(SHARED, 'Shared'),
		(PRIVATE, 'Private'),
		(MARRIED, 'Married'),
		)
	room_type = models.CharField(max_length=7, choices=ROOM_TYPE, default=PRIVATE)

