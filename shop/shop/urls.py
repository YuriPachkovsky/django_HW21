from django.contrib import admin
from django.urls import path, include
from shop.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls')),
    path('home/', index),

]
