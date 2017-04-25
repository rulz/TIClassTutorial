from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from log.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^calendar/', include('calendars.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}, name='logout'),
]
