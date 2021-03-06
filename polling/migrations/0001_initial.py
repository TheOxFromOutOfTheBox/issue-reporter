# Generated by Django 3.1.1 on 2020-10-01 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0009_auto_20200922_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=128)),
                ('department', models.CharField(blank=True, max_length=20)),
                ('join', models.CharField(blank=True, max_length=4)),
                ('active', models.BooleanField(default=True)),
                ('options', models.ManyToManyField(blank=True, null=True, to='polling.Option')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='profiles.userinfo')),
            ],
        ),
    ]
