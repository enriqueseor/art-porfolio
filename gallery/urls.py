from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.galleries, name='home'),
    re_path(r'^gallery/(?P<gallery_title_slug>[\w\-]+)/$', views.gallery_detail, name='gallery_detail'),
    re_path(r'^art/(?P<art_id>[0-9]+)/$', views.art_detail, name='art'),
    path('about/', views.about_me, name='aboutMe'),
]
