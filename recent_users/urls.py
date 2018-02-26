from django.conf.urls import url

from recent_users import views

urlpatterns = [
    url(r'^', views.twitter_users, name='users')
]