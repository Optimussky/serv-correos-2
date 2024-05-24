from rest_framework.serializers import ModelSerializer
from notification.models import Notification

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        #fields = '__all__' # Esto no es recomendable
        fields = ['uuid','body','email','title']


class NotificationSerializerV2(ModelSerializer):
    class Meta:
        model = Notification
        #fields = '__all__' # Esto no es recomendable
        fields = ['body','email','title','created']