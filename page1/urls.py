from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^rew/', views.index, name='index'),
    url(r'^form1/', views.send, name='send'),
]