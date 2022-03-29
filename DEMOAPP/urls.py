from django.contrib import admin
from django.urls import path
from DEMOAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name='login'),
    path('register', views.registerdata, name="reg"),
    path('guest/', views.guest, name='guest'),
    path('forgot/', views.forgotview, name='forgot'),
    path('Approve & Running Minute Save/', views.Approveview, name='Admin1'),
    path('Report Entry/', views.Entryview, name='Admin2'),
    path('CHP Shift Log/', views.CHP11view, name='CHP11'),

]