# Generated by Django 5.0.5 on 2024-05-09 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invista', '0002_investimento_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimento',
            name='nivel',
        ),
    ]
