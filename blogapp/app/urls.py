from django.urls import path
from . import views

urlpatterns = [
    path('x/', views.index, name='index'),
    path('ydf/a', views.myName, name='myNamxe'),
]