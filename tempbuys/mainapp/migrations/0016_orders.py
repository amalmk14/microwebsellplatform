# Generated by Django 4.1.2 on 2023-11-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_coupen_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('template_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment', models.CharField(blank=True, max_length=100)),
                ('finder', models.CharField(blank=True, max_length=100)),
                ('template_category', models.TextField(blank=True)),
                ('template_amount', models.TextField()),
                ('coupen_code', models.CharField(blank=True, max_length=20, null=True)),
                ('final_amount', models.IntegerField(default=0)),
                ('plan', models.CharField(blank=True, default=True, max_length=20)),
                ('amount_paid', models.BooleanField(default=False)),
            ],
        ),
    ]
