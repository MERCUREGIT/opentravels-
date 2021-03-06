# Generated by Django 3.0.5 on 2020-05-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_manager', '0002_trip_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip_data',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trip_data',
            name='Time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='trip_data',
            name='agency',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trip_data',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='trip_data',
            name='destination',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trip_data',
            name='origin',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trip_data',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
