# Generated by Django 3.0.3 on 2020-02-16 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200213_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'uma cor', 'verbose_name_plural': 'Cores'},
        ),
        migrations.AlterModelOptions(
            name='measure',
            options={'verbose_name': 'uma medida', 'verbose_name_plural': 'Medidas'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'um produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='reference',
            options={'verbose_name': 'uma referencia', 'verbose_name_plural': 'Referencias'},
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Cor'),
        ),
        migrations.AlterField(
            model_name='measure',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='measure',
            name='value',
            field=models.CharField(max_length=30, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Color', verbose_name='Cor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='product',
            name='measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Measure', verbose_name='Medida'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Preço de Compra'),
        ),
        migrations.AlterField(
            model_name='product',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Reference', verbose_name='Referencia'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Referencia'),
        ),
    ]
