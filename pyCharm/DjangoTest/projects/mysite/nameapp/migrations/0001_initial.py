# Generated by Django 3.1.3 on 2020-12-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KospiPredict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=10, unique=True, verbose_name='날짜')),
                ('close', models.FloatField(null=True, verbose_name='종가')),
                ('open', models.FloatField(null=True, verbose_name='시가')),
            ],
        ),
    ]
