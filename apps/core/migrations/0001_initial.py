# Generated by Django 3.0.3 on 2020-02-16 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogsLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='anonymo', max_length=150, verbose_name='Usuario')),
                ('type', models.CharField(max_length=15, verbose_name='Tipo')),
                ('ip', models.GenericIPAddressField(blank=True, default='127.0.0.1', null=True, verbose_name='IP')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'log login',
                'verbose_name_plural': 'Logs login',
            },
        ),
    ]
