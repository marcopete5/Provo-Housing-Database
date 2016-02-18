from __future__ import unicode_literals

from django.db import models

class Listing(models.Model):
    name = models.CharField(max_length=70)

    roommates = models.IntegerField()

    availability_date = models.DateField()

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

    FURNISHED = 'Furnished' 
    PARTIAL_FURNISHED = 'Partial Furnished' 
    UNFURNISHED = 'Unfurnished' 
    FURNISHINGS = (
        (FURNISHED,'Furnished'),
        (PARTIAL_FURNISHED, 'Partial Furnished'),
        (UNFURNISHED, 'Unfurnished'),
        ) 
    furnishings_type = models.CharField(max_length=20, choices=FURNISHINGS, default=UNFURNISHED) 

    FALL = 'Fall'
    SUMMER = 'Summer'
    WINTER = 'Winter'
    FALL_WINTER = 'Fall/Winter'
    WINTER_SUMMER = 'Winter/Summer'
    SUMMER_FALL = 'Summer/Fall'
    FULL_YEAR = 'Full Year'
    OTHER = 'Other'
    CONTRACT_LENGTH = (
        (FALL, 'Fall'),
        (SUMMER, 'Summer'),
        (WINTER, 'Winter'),
        (FALL_WINTER, 'Fall/Winter'),
        (WINTER_SUMMER, 'Winter/Summer'),
        (SUMMER_FALL, 'Summer/Fall'),
        (FULL_YEAR, 'Full Year'),
        (OTHER, 'Other'),
        )
    contract_length = models.CharField(max_length=15, choices=CONTRACT_LENGTH, default=FALL_WINTER)
    
    APARTMENT = 'Apt'
    HOUSE = 'House'
    BUILDING_TYPE = (
        (APARTMENT, 'Apartment'),
        (HOUSE, 'House'),
        )
    building_type = models.CharField(max_length=10, choices=BUILDING_TYPE, default=APARTMENT)
    
    BYU_housing = models.BooleanField(default=False)

    distance_from_universities = models.IntegerField()

    address = models.CharField(max_length=70)

    city = models.CharField(max_length=70)

    state = models.CharField(max_length=70)

    selling_price = models.IntegerField()



