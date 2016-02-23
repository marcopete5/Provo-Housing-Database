
from django.conf.urls import url
from django.contrib import admin
from main.views import Main, ApptComplexDetailView, ApptListingDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', Main.as_view()),
    url(r'^testing/$','main.views.appartment_complex'),
    url(r'^testing/(?P<pk>\d+)/$', ApptComplexDetailView.as_view()),
    url(r'^listing/(?P<pk>\d+)/$', ApptListingDetailView.as_view()),
]