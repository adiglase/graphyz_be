import json

from rest_framework import serializers

from charts.models import Chart, CHART_TYPES


class ChartTypeSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    icon = serializers.SerializerMethodField()

    def get_icon(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri('/') + obj['icon']


class UserChartListSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    icon = serializers.SerializerMethodField()
    chart_type = serializers.CharField()

    def get_icon(self, obj):
        chart_icon_url = CHART_TYPES[obj.chart_type]['icon']
        request = self.context.get('request')
        return request.build_absolute_uri('/') + chart_icon_url

    class Meta:
        model = Chart
        fields = ['id', 'title', 'icon', 'chart_type']


class CreateChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = ['id', 'title', 'data_file', 'chart_type', 'label', 'value']


class RetrieveChartSerializer(serializers.ModelSerializer):
    column_configuration_options = serializers.SerializerMethodField()
    chart_visualization = serializers.SerializerMethodField()

    def get_column_configuration_options(self, obj):
        return obj.get_column_configuration_options()

    def get_chart_visualization(self, obj):
        chart_visualization = obj.get_chart_visualization()
        return json.loads(chart_visualization) if chart_visualization else None

    class Meta:
        model = Chart
        fields = ['title', 'chart_type', 'label', 'value', 'column_configuration_options', 'chart_visualization']


class UpdateChartSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    data_file = serializers.FileField(allow_null=True, allow_empty_file=True, required=False)
    label = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    value = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    column_configuration_options = serializers.SerializerMethodField()
    chart_visualization = serializers.SerializerMethodField()


    def get_column_configuration_options(self, obj):
        print(obj.get_column_configuration_options())
        return obj.get_column_configuration_options()

    def get_chart_visualization(self, obj):
        chart_visualization = obj.get_chart_visualization()
        return json.loads(chart_visualization) if chart_visualization else None

    class Meta:
        model = Chart
        fields = ['title', 'data_file', 'label', 'value', 'column_configuration_options', 'chart_visualization']
