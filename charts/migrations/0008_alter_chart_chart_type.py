# Generated by Django 4.1.2 on 2022-12-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0007_alter_chart_data_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='chart_type',
            field=models.CharField(choices=[('BC', 'Bar Chart'), ('LC', 'Line Chart'), ('PC', 'Pie Chart')], max_length=255),
        ),
    ]
