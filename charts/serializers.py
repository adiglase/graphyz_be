from rest_framework import serializers

from charts.models import Chart


class ChartTypeSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    icon = serializers.SerializerMethodField()

    def get_icon(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri('/') + obj['icon']


class CreateChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = ['id', 'title', 'data_file', 'chart_type', 'label', 'value']


class RetrieveChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = ['title', 'chart_type', 'label', 'value']


class UpdateChartSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    data_file = serializers.FileField(allow_null=True, allow_empty_file=True, required=False)
    label = serializers.CharField(allow_blank=True, allow_null=True)
    value = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Chart
        fields = ['title', 'data_file', 'label', 'value']
