from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from notification.models import Notification
from . notification.serializers import NotificationSerializer


class NotificationAPIView(APIView):
    def get(self, request):
        serializer = NotificationSerializer(Notification.objects.all(),many=True)
    
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    def post(self, request):
        serializer = NotificationSerializer(data=request.Notification)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK, data=serializer.data)

        