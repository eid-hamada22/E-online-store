# Generated by Django 4.0.6 on 2022-07-25 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_product_ar_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='similar_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='bio',
            field=models.TextField(max_length=100, verbose_name='bio    <li></li>   '),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_image',
            field=models.ManyToManyField(blank=True, max_length=3, to='pages.secondary_image'),
        ),
    ]
