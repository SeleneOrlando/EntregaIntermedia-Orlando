# Generated by Django 4.1.2 on 2022-11-13 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='fechacrracion',
            field=models.DateField(null=True),
        ),
    ]
