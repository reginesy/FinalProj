# Generated by Django 2.0.4 on 2018-04-30 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteminstance',
            name='imprint',
        ),
    ]
