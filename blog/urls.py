from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list), # It forwards to initial page
]