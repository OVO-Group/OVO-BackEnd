# Generated by Django 5.0.2 on 2024-05-29 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovo', '0014_rename_id_comanda_id_comanda_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data',
            field=models.DateField(default='2024-05-12'),
        ),
    ]