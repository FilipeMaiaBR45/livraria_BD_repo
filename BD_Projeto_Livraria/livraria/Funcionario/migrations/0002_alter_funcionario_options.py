# Generated by Django 3.2 on 2021-04-20 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'ordering': ['nome']},
        ),
    ]