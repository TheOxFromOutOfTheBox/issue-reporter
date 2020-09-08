# Generated by Django 3.1.1 on 2020-09-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0004_report_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-updated', '-timestamp']},
        ),
        migrations.AddField(
            model_name='report',
            name='year',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
