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
    column_configuration_options = serializers.SerializerMethodField()

    def get_column_configuration_options(self, obj):
        return obj.get_column_configuration_options()

    class Meta:
        model = Chart
        fields = ['title', 'chart_type', 'label', 'value', 'column_configuration_options']


class UpdateChartSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    data_file = serializers.FileField(allow_null=True, allow_empty_file=True, required=False)
    label = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    value = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    column_configuration_options = serializers.SerializerMethodField()

    def get_column_configuration_options(self, obj):
        return obj.get_column_configuration_options()

    class Meta:
        model = Chart
        fields = ['title', 'data_file', 'label', 'value', 'column_configuration_options']
