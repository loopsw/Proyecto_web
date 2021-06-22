# Generated by Django 3.2.3 on 2021-05-26 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='services', verbose_name='Seleccione imagen')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('content', models.TextField(max_length=300, verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creada el')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Última actualización')),
                ('status', models.CharField(choices=[('publicado', 'pubished'), ('borrador', 'draft')], default='borrador', max_length=10, verbose_name='Estado')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
