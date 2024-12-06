from rest_framework import serializers
from datetime import timedelta
from django.utils.timezone import now
from .models import URL
from .helpers.helper import validate_url

class URLShortenerSerializer(serializers.ModelSerializer):
    TTL = serializers.IntegerField(min_value=1, required=False)
    class Meta:
        model = URL
        fields = ('original_url', 'TTL')

    def validate_original_url(self, value):
        try:
            validate_url(value)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        return value
    
    def create(self, validated_data):
        ttl = validated_data.pop('TTL', None)
        expires_at = now() + timedelta(days=ttl) if ttl else None
        url_instance = URL.objects.create(expires_at=expires_at, **validated_data)
        return url_instance
    
class CustomURLShortenerSerializer(serializers.ModelSerializer):
    TTL = serializers.IntegerField(min_value=1, required=False)
    class Meta:
        model = URL
        fields = ('original_url', 'short_url', 'TTL')
    
class URLStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('short_url', )

    # def validate_short_url(self, value):
    #     if not URL.objects.filter(short_url=value).exists():
    #         raise serializers.ValidationError("Invalid short URL")
    #     return value
