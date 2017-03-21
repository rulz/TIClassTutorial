from django.conf.urls import url
from . import views

urlpatterns = [
    # /calendar/
    url(r'^$', views.index, name = 'index'),

    # /calendar/form/
    url(r'^form/', views.form, name = 'form')

]