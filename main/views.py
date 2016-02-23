from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import ComplexName, Listing

class Main(TemplateView):

	template_name = "base.html"

#class Testing(TemplateView):
#   template_name = "testing.html"

def appartment_complex(request):
	complex_name = ComplexName.objects.all()
	house_listings = Listing.objects.filter(apartment_complex=False)

	context = {}

	context['complex_list'] = complex_name
	context['house_list'] = house_listings



	return render(request, 'testing.html', context)


class ApptComplexDetailView(DetailView):
	model = ComplexName
	template_name = "testing_two.html"
	context_object_name = "appartment"


class ApptListingDetailView(DetailView):
	model = Listing
	template_name = "testing_three.html"
	context_object_name = "listing"