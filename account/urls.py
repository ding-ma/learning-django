from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^api/account/signup$', views.create_account),
    url(r'^api/account/modifications$', views.modify_account),
    url(r'^api/account/login$', views.login),
]
