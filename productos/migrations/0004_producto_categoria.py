# Generated by Django 5.1.4 on 2025-03-06 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_datos'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Hombre', max_length=10),
        ),
    ]
