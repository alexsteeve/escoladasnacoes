# Generated by Django 2.1 on 2018-09-01 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0010_cursoperiodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursoperiodo',
            name='diaSemana',
            field=models.CharField(default='Domingo', max_length=255),
        ),
    ]