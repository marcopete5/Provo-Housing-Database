from __future__ import unicode_literals
from django.db import models
from housing.local_settings import local_GoogleAPI_key

import googlemaps

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

    
    amenity = models.ManyToManyField('Amenities')

	apartment_complex = models.BooleanField(default=True)

	complex_name = models.ForeignKey('ComplexName', blank=True, null=True)

	distance_from_BYU = models.FloatField(null=True, blank=True, editable=False)

	distance_from_UVU = models.FloatField(null=True, blank=True, editable=False)

	address = models.CharField(max_length=70)

	city = models.CharField(max_length=70)

	state = models.CharField(max_length=70)

	selling_price = models.IntegerField()

	description = models.TextField()

	upload_image = models.ImageField(null=True, blank=True)

	def __unicode__(self):
		return self.address

	def save(self):
		gmaps = googlemaps.Client(key=local_GoogleAPI_key)	
		
		googleAPI_dict_BYU = gmaps.distance_matrix("%s %s %s" % (self.address,self.city,self.state), "155 East 1230 North, Provo, UT" )
		googleAPI_dict_UVU = gmaps.distance_matrix("%s %s %s" % (self.address,self.city,self.state), "800 W. University Pkwy, Orem, Utah 84058" )


		tempBYU = (googleAPI_dict_BYU['rows'][0]['elements'][0]['distance']['text']) #from google API
		tempUVU = (googleAPI_dict_UVU['rows'][0]['elements'][0]['distance']['text'])
		
		def str_to_miles_convert(temp1):
			temp1 = temp1.split() #temp1 '413 km' as example
			dist_in_miles = round((float(temp1[0])*.621371), 1)
			return dist_in_miles


		self.distance_from_BYU = str_to_miles_convert(tempBYU)
		print "dist %d" % self.distance_from_BYU
		self.distance_from_UVU = str_to_miles_convert(tempUVU)

		super(Listing, self).save()


	

class Amenities(models.Model):
	amenity = models.CharField(max_length=20)

	def __unicode__(self):
		return self.amenity

	class Meta:
		verbose_name_plural = 'amenities'

class ComplexName(models.Model):
	name = models.CharField(max_length=40)

	def __unicode__(self):
		return self.name


# google api key AIzaSyB5UvPtsN-s6PXF2xiXg7Vb18y1dQm1McU




