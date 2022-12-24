from rest_framework import serializers


class ChartTypeSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    icon = serializers.SerializerMethodField()

    def get_icon(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri('/') + obj['icon']
