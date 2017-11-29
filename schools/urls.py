from django.conf.urls import url
from .views import view_school, do_search

urlpatterns = [
    
    url(r'^school/(.+)$', view_school, name="view_school"),
     url(r'^search/', do_search, name="search"),

 ]