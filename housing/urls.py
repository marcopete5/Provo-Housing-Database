
from django.conf.urls import url
from django.contrib import admin
from main.views import Main, Testing

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', Main.as_view()),
    url(r'^testing/',Testing.as_view()),
]


