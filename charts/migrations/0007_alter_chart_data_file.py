# Generated by Django 4.1.2 on 2022-12-26 13:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0006_alter_chart_data_file_alter_chart_label_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='data_file',
            field=models.FileField(blank=True, null=True, upload_to='data/', validators=[django.core.validators.FileExtensionValidator(['xlsx'])], verbose_name='Data'),
        ),
    ]