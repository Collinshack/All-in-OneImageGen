from rest_framework import serializers
from users.models import Image, CustomUser


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('prompt', 'generated_image')
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
        