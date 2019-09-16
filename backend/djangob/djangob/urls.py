"""djangob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from tangun import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tangun/', include('tangun.urls')),
    path('send_data_list/', views.send_data_list),
    path('get_data_list/', views.get_data_list),
    path('get_data_fee/', views.get_data_fee),
    path('send_data_fee/', views.send_data_fee),
    path('get_data_payment_custom/', views.get_data_payment_custom),
    path('save_custom_payments/', views.save_custom_payments),
    path('get_map/', views.get_map),
    path('fill_payments/', views.fill_payments),
]