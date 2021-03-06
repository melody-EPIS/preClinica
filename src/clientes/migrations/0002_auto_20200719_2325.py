# Generated by Django 2.1.5 on 2020-07-20 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('celular', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='correo',
            new_name='usuario',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(max_length=100),
        ),
    ]
