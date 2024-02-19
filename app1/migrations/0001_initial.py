# Generated by Django 4.0.5 on 2022-07-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='patron',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=30)),
                ('seccion', models.CharField(max_length=30)),
                ('algoritmo', models.CharField(max_length=30)),
                ('comentarios', models.CharField(max_length=100, null=True)),
                ('usuario', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]