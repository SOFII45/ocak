from rest_framework import serializers
from .models import Project
from martyrs.models import Martyr # Diğer uygulamadan (app) doğru çağırma yolu

class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'short_description', 
            'image', 'image_url', 'project_link', 'start_date', 
            'end_date', 'status', 'budget', 'location', 'is_active'
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

class ProjectListSerializer(ProjectSerializer):
    class Meta(ProjectSerializer.Meta):
        fields = ['id', 'title', 'short_description', 'image_url', 'status', 'project_link']