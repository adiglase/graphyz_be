# Generated by Django 4.1.2 on 2022-12-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charttype',
            name='type',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='charttype',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]