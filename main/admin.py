from django.contrib import admin
from .models import ComplexName, Amenities, Listing

admin.site.register(Listing)
admin.site.register(Amenities)
admin.site.register(ComplexName)