# Generated by Django 3.0 on 2020-01-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attapp', '0019_auto_20200106_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud_attendance',
            name='batch',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
