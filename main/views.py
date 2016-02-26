from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.core import serializers
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .forms import ListingForm
from .models import ComplexName, Listing


#class Testing(TemplateView):
#   template_name = "testing.html"

def housing_API_view(request):
	request.method == 'POST'

	complexes = ComplexName.objects.all()
	listings = Listing.objects.filter(apartment_complex=False)

	complex_output = serializers.serialize('json', complexes, fields=('name', 'address'))
	listings_output = serializers.serialize('json', listings, fields=('name', 'address', 'city', 'state'))

	output = [complex_output,listings_output]

	return HttpResponse(output, content_type='application/json')



def home(request):
	complex_name = ComplexName.objects.all()
	house_listings = Listing.objects.filter(apartment_complex=False)

	context = {}

	context['complex_list'] = complex_name
	context['house_list'] = house_listings

	print "house list %s" % context['house_list']
	print "complex list %s" % context['complex_list']


	return render(request, 'both_list_views.html', context)


class AptComplexDetailView(DetailView):
	model = ComplexName
	template_name = "both_list_views.html"
	context_object_name = "complex"


class AptListingDetailView(DetailView):
	model = Listing
	template_name = "detail_view.html"
	context_object_name = "listing"


class ListingCreateView(CreateView):
	form_class = ListingForm
	template_name = "post.html"








