# Generated by Django 4.1.6 on 2023-02-04 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bicicletas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=150)),
                ('modelo', models.CharField(max_length=150)),
                ('tamanho', models.CharField(max_length=150)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]
