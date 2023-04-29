# Generated by Django 4.0.3 on 2022-03-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_user_name_user_fname_user_lname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('published_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('Brand', models.CharField(max_length=10)),
                ('bio', models.TextField(max_length=100)),
                ('price', models.IntegerField(max_length=10)),
                ('lprice', models.IntegerField(max_length=10)),
                ('Discount', models.IntegerField(max_length=10)),
            ],
        ),
    ]