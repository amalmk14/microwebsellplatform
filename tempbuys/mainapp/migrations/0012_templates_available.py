# Generated by Django 4.1.2 on 2023-11-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_rename_types_templates_temp_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
