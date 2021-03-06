# Generated by Django 2.2.11 on 2020-03-15 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Demanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição da peça')),
                ('cep', models.CharField(blank=True, max_length=9)),
                ('numero', models.CharField(blank=True, max_length=5)),
                ('logradouro', models.CharField(blank=True, max_length=230)),
                ('bairro', models.CharField(blank=True, max_length=230)),
                ('email', models.EmailField(blank=True, max_length=45)),
                ('telefone', models.CharField(blank=True, max_length=14)),
                ('status', models.BooleanField(choices=[(False, 'Aberto'), (True, 'Finalizado')], default=False, max_length=1)),
                ('anunciante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
