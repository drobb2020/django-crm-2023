from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>/', views.customer_record, name='record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete'),
    path('create_record/', views.create_record, name='create'),
    path('update_record/<int:pk>/', views.update_record, name='update'),
]
