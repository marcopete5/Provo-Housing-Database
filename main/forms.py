from django import forms
from .models import Listing
from datetimewidget.widgets import DateWidget


class ListingForm(forms.ModelForm):
	class Meta:
		model = Listing
		widgets = {'availability_date':DateWidget(attrs={'id':"yourdateid"}, usel10n = True, bootstrap_version=3)}
		fields = ['name', 'roommates', 'availability_date', 'gender_choices','room_type', 'furnishings_type', 'contract_length', 'building_type', 'BYU_housing', 'amenity', 'apartment_complex', 'complex_name', 'address', 'apt_number', 'city', 'state', 'selling_price', 'description', 'upload_image', 'deposit']
		