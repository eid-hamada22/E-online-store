# Generated by Django 4.0.3 on 2022-07-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_det_delete_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='det',
            name='type',
            field=models.CharField(choices=[('phones', 'phones')], max_length=250),
        ),
    ]
