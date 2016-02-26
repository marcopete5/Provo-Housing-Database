
from django.conf.urls import url
from django.contrib import admin
from main.views import home, AptComplexDetailView, AptListingDetailView, ListingCreateView


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', 'main.views.home'),
	#url(r'^complex/$','main.views.appartment_complex'),
	url(r'^complex/(?P<pk>\d+)/$', AptComplexDetailView.as_view()),
	url(r'^listing/(?P<pk>\d+)/$', AptListingDetailView.as_view()),
	url(r'^listingcreate/$', ListingCreateView.as_view()),
	url(r'^housing_api/', 'main.views.housing_API_view'),
]