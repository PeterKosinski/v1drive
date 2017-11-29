from django.conf.urls import url
from .views import blogposts, viewpost

urlpatterns = [
    url(r'^posts$', blogposts, name="blogposts"),
    url(r'^post/(.+)$', viewpost, name="viewpost")
 ]