# Generated by Django 4.1.3 on 2023-03-21 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audioguideapp', '0037_remove_payment_monument_id_remove_payment_receipt_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='monument_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='audioguideapp.monument'),
        ),
    ]
