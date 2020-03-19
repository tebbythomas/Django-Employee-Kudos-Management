# Generated by Django 3.0.4 on 2020-03-19 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20200319_0008'),
        ('profiles', '0004_auto_20200319_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
    ]
