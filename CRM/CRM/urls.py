"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$',views.index_view),
    url(r'^table/',views.table_view,name='home'),
    url(r'^home/', views.home_view),
    url(r'^order/', views.order_view),
    url(r'^help/', views.help_view),
    url(r'^register/', views.registerPage, name='register'),
    url(r'^login/',views.loginPage,name='login'),
    url(r'^logout/', views.logoutUser, name='logout'),
    url(r'^user/', views.userPage, name='user-page'),
#------------------------------Account----------------------------------------------
    url(r'^account/', views.account, name='account'),
    url(r'^create_account/', views.create_account_view, name='create'),
    path('update_account/<str:pk>/', views.updateAccount, name="update_account"),
    path('delete_account/<str:pk>/', views.delete_account, name="delete_account"),

#------------------------------Contact----------------------------------------------
    url(r'^contact/', views.contact,name='contact'),
    url(r'^create_contact/', views.create_contact, name='create_contact'),
    path('update_contact/<str:pk>/', views.updateContact, name="update_contact"),
    path('delete_contact/<str:pk>/', views.delete_contact, name="delete_contact"),

]
