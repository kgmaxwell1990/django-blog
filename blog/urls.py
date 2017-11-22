from django.conf.urls import url
from .views import blogposts, viewpost, newpost, editpost, deletepost, addcomment

urlpatterns = [
    url(r'^posts$', blogposts, name="posts"),
    url(r'^posts/add', newpost, name="newpost"),
    url(r'^posts/(.+)/edit$', editpost, name="editpost"),
    url(r'^posts/(.+)/delete$', deletepost, name="deletepost"),
    url(r'^posts/(.+)/comments/add$', addcomment, name="addcomment"),
    url(r'^posts/(.+)$', viewpost, name="viewpost"),
    ]
