# Generated by Django 5.0.3 on 2024-03-06 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='celular',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]