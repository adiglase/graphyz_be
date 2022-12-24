from django.core.validators import FileExtensionValidator
from django.db import models

from users.models import User


CHART_TYPES = {
    'BC': {
        'name': 'Bar Chart',
        'icon': 'media/assets/icons/bar-chart.svg',
        'id': 'BC'
    },
    'LC': {
        'name': 'Line Chart',
        'icon': 'media/assets/icons/line-chart.svg',
        'id': 'LC'
    },
    'PC': {
        'name': 'Pie Chart',
        'icon': 'media/assets/icons/pie-chart.svg',
        'id': 'PC'
    }
}

CHART_TYPE_CHOICES = [(CHART_TYPES[chart_type_id]['id'], CHART_TYPES[chart_type_id]['name']) for
                      chart_type_id in CHART_TYPES]


class Chart(models.Model):
    created_by = models.ForeignKey(User, related_name="charts", null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, default='Untitled')
    data_file = models.FileField("Data", upload_to='data/', validators=[FileExtensionValidator(['xlsx'])])
    chart_type = models.CharField(choices=CHART_TYPE_CHOICES, max_length=5)
    label = models.CharField(max_length=10)
    value = models.CharField(max_length=10)
