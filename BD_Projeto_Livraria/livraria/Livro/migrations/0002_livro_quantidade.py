# Generated by Django 3.2 on 2021-04-20 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Livro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]