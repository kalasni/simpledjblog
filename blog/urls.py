from django.conf.urls import include, url
from . import views


# name='name_view' is the view's name where we want to go.
urlpatterns = [
        url(r'^$', views.post_list, name='post_list'), # It forwards to initial page
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
        url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
        url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
        url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

]