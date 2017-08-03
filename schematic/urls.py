from django.conf.urls import url
from schematic import views
urlpatterns = [

    url(r'^$', views.home),
    url(r'^num/(?P<a>\d+)/(?P<b>[a-z]*)$',views.test),
    url(r'^fsf$',views.haha),
    url(r'^date$',views.today),
    url(r'^blog$',views.blog)

]