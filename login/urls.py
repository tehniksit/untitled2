from django.conf.urls import url
from django.contrib import admin
from login import views


admin.autodiscover()

urlpatterns = [
    url(r'^$', views.login, name='login'),

]
