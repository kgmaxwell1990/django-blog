from django.conf.urls import url
from .views import blogposts

urlpatterns = [
    url(r'^posts', blogposts, name="posts"),
    ]