# Generated by Django 4.1.2 on 2022-12-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0008_alter_chart_chart_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='chart_type',
            field=models.CharField(choices=[('BC', 'Bar Chart'), ('LC', 'Line Chart'), ('PC', 'Pie Chart')], max_length=5),
        ),
        migrations.AlterField(
            model_name='chart',
            name='label',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='chart',
            name='value',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
