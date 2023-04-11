# Generated by Django 4.2 on 2023-04-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('nombre_del_auto', models.CharField(max_length=20)),
                ('kilometros_recorridos', models.IntegerField()),
                ('detalles_auto', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='animales',
        ),
        migrations.DeleteModel(
            name='persona',
        ),
    ]
