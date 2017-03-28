from django.conf.urls import url
from . import views


urlpatterns = [
    # /calendar/
    url(r'^$', views.index, name = 'index'),

    # /calendar/create/
    url(r'^create/$', views.calendar_create, name = 'calendar_create'),

    # /calendar/id/
    url(r'^(?P<pk>[-\d]+)/detail/$', views.calendar_detail, name='calendar_detail'),

    # /calendar/delete/
    url(r'^(?P<pk>[-\d]+)/delete/$', views.calendar_delete, name='calendar_delete'),

    # /calendar/delete/done
    url(r'^delete/done/$', views.delete_confirm, name='calendar_delete_confirm'),

    # /calendar/edit/
    url(r'^(?P<pk>[-\d]+)/edit/$', views.calendar_edit, name='calendar_edit'),

    # /calendar/edit/done
    url(r'^edit/done/$', views.edit_confirm, name='calendar_edit_confirm'),

    # /calendar/list/
    url(r'^list/$', views.calendar_list, name='calendar_list'),
]
