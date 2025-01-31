# Generated by Django 3.0.3 on 2020-02-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_auto_20200213_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detached',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('purchase_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ManyToManyField(to='product.Product')),
            ],
        ),
    ]
