from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^data-science$', views.datascience, name='datascience'),
    url(r'^raw/data-science$', views.raw_datascience, name='raw_datascience'),
]
