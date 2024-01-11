from django.urls import path
from .views import post_list, create_post
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),

    # path('',views.index,name="index"),
    # path('add/',views.add,name="add"),
]
