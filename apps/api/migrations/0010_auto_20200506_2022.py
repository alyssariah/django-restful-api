# Generated by Django 3.0.6 on 2020-05-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200506_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlog',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
