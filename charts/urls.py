from django.urls import path
from rest_framework import routers

from charts.views import ListChartTypes, ChartViewSet

router = routers.DefaultRouter()
router.register("charts", ChartViewSet, basename="charts")

urlpatterns = [
    path('chart-types/', ListChartTypes.as_view(), name='chart-type-list')
]
urlpatterns += router.urls
