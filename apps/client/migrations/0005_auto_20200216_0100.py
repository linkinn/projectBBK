# Generated by Django 3.0.3 on 2020-02-16 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20200216_0100'),
        ('client', '0004_auto_20200213_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'um client', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Address', verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='client',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='client',
            name='cpf',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=250, verbose_name='Primeiro Nome'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Ultimo Nome'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='client',
            name='rg',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='RG'),
        ),
    ]
