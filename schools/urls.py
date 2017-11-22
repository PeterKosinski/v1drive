from django.conf.urls import url
from .views import view_school

urlpatterns = [
    
    url(r'^school/(\d+)$', view_school, name="view_school"),

 ]