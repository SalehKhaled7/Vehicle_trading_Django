"""carsite URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('cars/', include('cars.urls')),
    path('aboutus/', views.about_us, name='about_us'),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('buy/', views.buy_a_car, name='cars'),
    path('buy/<int:id>/<slug:slug>', views.buy_a_car, name='buy_a_car'),
    path('car/<int:id>/<slug:slug>', views.car_details, name='car_details'),
    path('search/', views.car_search, name='car_search'),
    path('search_auto/',views.car_search_auto, name='car_search_auto'),
    path('logout/',views.logout_view, name='logout_view'),
    path('login/',views.login_view, name='login_view'),

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
