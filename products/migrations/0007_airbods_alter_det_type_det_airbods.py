# Generated by Django 4.0.6 on 2022-07-20 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_phones_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='airbods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('det_id', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='')),
                ('version', models.CharField(blank=True, max_length=250, null=True)),
                ('internal_memory', models.CharField(blank=True, max_length=250, null=True)),
                ('model_color', models.CharField(blank=True, max_length=250, null=True)),
                ('sim_nm', models.IntegerField(blank=True, null=True)),
                ('g_type', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='det',
            name='type',
            field=models.CharField(choices=[('phones', 'phones'), ('airbods', 'airbods')], max_length=250),
        ),
        migrations.AddField(
            model_name='det',
            name='airbods',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.airbods'),
        ),
    ]