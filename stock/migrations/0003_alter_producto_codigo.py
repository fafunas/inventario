# Generated by Django 3.2.5 on 2021-08-25 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_remove_tipo_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Codigo'),
        ),
    ]
