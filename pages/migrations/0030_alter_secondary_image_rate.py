# Generated by Django 4.0.6 on 2022-07-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_alter_product_secondary_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondary_image',
            name='rate',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)]),
        ),
    ]
