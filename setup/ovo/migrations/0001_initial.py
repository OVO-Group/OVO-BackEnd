# Generated by Django 5.0.3 on 2024-03-06 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=45)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('celular', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id_endereco', models.AutoField(primary_key=True, serialize=False)),
                ('nome_da_rua', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=7)),
                ('complemento', models.CharField(max_length=45)),
                ('ponto_de_referencia', models.CharField(max_length=100)),
                ('favorito', models.BinaryField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ovo.usuario')),
            ],
        ),
    ]
