# Generated by Django 4.1.2 on 2023-11-30 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_remove_orders_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentSuccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('expiry_date', models.DateTimeField()),
                ('countdown', models.IntegerField(default=0)),
                ('payment_status', models.BooleanField(default=False)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.orders')),
            ],
        ),
    ]
