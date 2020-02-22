# Generated by Django 3.0.3 on 2020-02-22 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApellidoPaterno', models.CharField(max_length=35)),
                ('ApellidoMaterno', models.CharField(max_length=35)),
                ('Nombres', models.CharField(max_length=35)),
                ('DNI', models.CharField(max_length=8)),
                ('FechaNacimiento', models.DateField()),
                ('Sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Creditos', models.PositiveSmallIntegerField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaMatricula', models.DateTimeField(auto_now_add=True)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.Alumno')),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.Curso')),
            ],
        ),
    ]
