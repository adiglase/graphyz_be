from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from charts.models import CHART_TYPES, Chart
from charts.serializers import ChartTypeSerializer, RetrieveChartSerializer, CreateChartSerializer, \
    UpdateChartSerializer


class ListChartTypes(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        chart_type_list = [chart_type_detail for chart_type_id, chart_type_detail in CHART_TYPES.items()]
        serialized_data = ChartTypeSerializer(chart_type_list, many=True, context={'request': request})
        return Response(serialized_data.data)


class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateChartSerializer
        if self.action == 'update':
            print('going here')
            return UpdateChartSerializer
        return RetrieveChartSerializer

    def update(self, request, *args, **kwargs):
        # only update that use formdata so we use different parser
        self.parser_classes = (MultiPartParser, FormParser)
        return super().update(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def get_data_file_in_dict(self, request, pk=None):
        chart = self.get_object()
        return Response(data=chart.get_data_file_in_dict())
