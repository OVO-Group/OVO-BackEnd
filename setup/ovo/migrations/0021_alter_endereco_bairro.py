# Generated by Django 5.0.2 on 2024-05-30 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovo', '0020_merge_20240530_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(default='Cocaia', max_length=45),
        ),
    ]
