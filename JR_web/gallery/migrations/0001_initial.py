# Generated by Django 3.2.3 on 2021-05-26 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Album')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='portfolio', verbose_name='Seleccione imagen')),
                ('name', models.CharField(max_length=100, verbose_name='Titulo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creada el')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Última actualización')),
                ('status', models.CharField(choices=[('activa', 'Activa'), ('inactiva', 'Inactiva')], default='inactiva', max_length=10, verbose_name='Estado')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.album', verbose_name='Album')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]