from django.conf.urls import url
from . import views

app_name = 'categories'

urlpatterns = [
    url(r'^$', views.category_list, name="list"),
    url(r'^create/$', views.category_create, name="create"),
    url(r'^edit/(?P<id>[\w-]+)/$', views.category_edit, name="edit"),
    url(r'^delete/(?P<id>[\w-]+)/$', views.category_delete, name="delete"),
]
