from django.conf.urls import url, include
import views
urlpatterns = [
    url(r'^$', views.post_list, name='blog')
]