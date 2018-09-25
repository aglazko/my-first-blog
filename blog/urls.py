from django.conf.urls import url
from . import views

#name='post_list' — это имя URL, которое будет использовано, чтобы идентифицировать его
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]