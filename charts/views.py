from rest_framework.response import Response
from rest_framework.views import APIView

from charts.models import CHART_TYPES
from charts.serializers import ChartTypeSerializer


class ListChartTypes(APIView):
    def get(self, request):
        chart_type_list = [chart_type_detail for chart_type_id, chart_type_detail in CHART_TYPES.items()]
        serialized_data = ChartTypeSerializer(chart_type_list, many=True, context={'request': request})
        return Response(serialized_data.data)
