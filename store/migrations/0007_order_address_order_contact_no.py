# Generated by Django 4.2.16 on 2024-11-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='order',
            name='contact_no',
            field=models.CharField(default='', max_length=14),
        ),
    ]
