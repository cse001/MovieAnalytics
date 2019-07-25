from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='welcome'),
    path('index',views.hello,name="dash"),
    path('view',views.processReq,name="hi")
]
