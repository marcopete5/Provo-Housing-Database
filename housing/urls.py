
from django.conf.urls import url, include
from django.contrib import admin
from main.views import home, AptComplexDetailView, AptListingDetailView, ListingCreateView
from django.conf import settings 


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', 'main.views.home'),
	#url(r'^complex/$','main.views.appartment_complex'),
	url(r'^complex/(?P<pk>\d+)/$', AptComplexDetailView.as_view()),
	url(r'^listing/(?P<pk>\d+)/$', AptListingDetailView.as_view()),
	url(r'^listingcreate/$', ListingCreateView.as_view()),
	url(r'^housing_api/', 'main.views.housing_API_view'),
	url(r'^media/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^single_complex/(?P<pk>\d+)/$', 'main.views.list_units_in_complex'),
	url(r'^accounts/$', 'main.views.home'),
	url(r'^accounts/', include('allauth.urls')),
]