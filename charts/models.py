from django.core.validators import FileExtensionValidator
from django.db import models
import pandas as pd

from users.models import User


class ChartManager(models.Manager):
    def get_data_file_json(self):
        return self.title


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
    data_file = models.FileField("Data", upload_to='data/', blank=True, null=True,
                                 validators=[FileExtensionValidator(['xlsx'])])
    chart_type = models.CharField(choices=CHART_TYPE_CHOICES, max_length=5)
    label = models.CharField(max_length=10, blank=True)
    value = models.CharField(max_length=10, blank=True)

    objects = ChartManager()

    def get_data_file_in_dict(self):
        if self.data_file:
            df = pd.read_excel(self.data_file)
            return df.to_dict(orient='records')
        return []
