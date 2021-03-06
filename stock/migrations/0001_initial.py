# Generated by Django 3.2.5 on 2021-08-26 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, verbose_name='Codigo')),
                ('descripcion', models.CharField(max_length=30, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'db_table': 'Grupos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, verbose_name='Codigo')),
                ('descripcion', models.CharField(max_length=30, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'Tipos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Codigo')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
                ('date_created', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.product_group')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.tipo')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Productos',
                'ordering': ['id'],
            },
        ),
    ]
