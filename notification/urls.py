from django.urls import path
from . views import NotificationAPIView


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('notification/', NotificationAPIView.as_view()),
]
