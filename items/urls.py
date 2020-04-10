from django.conf.urls import url
from . import views

app_name = 'items'

urlpatterns = [
    url(r'^$', views.item_list, name="list"),
    url(r'^create/$', views.item_create, name="create"),
    url(r'^edit/(?P<id>[\w-]+)/$', views.item_edit, name="edit"),
    url(r'^delete/(?P<id>[\w-]+)/$', views.item_delete, name="delete"),
]