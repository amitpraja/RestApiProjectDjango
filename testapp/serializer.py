from rest_framework import serializers
from testapp.models import client,project


class clientserializers(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = "__all__"

class projectserializers(serializers.ModelSerializer):
    clients = clientserializers(read_only=True , many= True)
    class Meta:
        model = project
        fields  = '__all__'