from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('serviceRequest', views.serviceRequest, name='serviceRequest'),
    path('feedback',views.feedback,name="feedback"),
]