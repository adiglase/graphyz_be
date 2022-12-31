import pandas as pd
import plotly.express as px


class ChartVisualization:
    def __init__(self, chart_type, label, value, data_file):
        self.chart_type = chart_type
        self.label = label
        self.value = value
        self.data_file = data_file

    def get_chart_visualization(self):
        df = pd.read_excel(self.data_file)

        if self.chart_type == 'BC':
            fig = px.bar(df, x=self.label, y=self.value, color=self.label)
        elif self.chart_type == 'LC':
            fig = px.line(df, x=self.label, y=self.value)

        # return fig.to_html(include_plotlyjs='require', full_html=False)
        return fig.to_json(pretty=True)
