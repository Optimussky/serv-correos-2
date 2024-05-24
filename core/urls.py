from django.contrib import admin
from django.urls import path, include
#from notification.views import HelloWorld
from notification.views import NotificationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('notification.urls')),
]


"""


"""
