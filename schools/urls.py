from django.conf.urls import url, include
from .views import view_school, do_search, all_schools


urlpatterns = [
    
    url(r'^$', all_schools, name="all_schools"),
    url(r'^school/(.+)$', view_school, name="view_school"),
    url(r'^search/', do_search, name="search"),
   

 ]