# Generated by Django 4.0.3 on 2022-03-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc18y2h', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('Username', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Username')),
                ('Email', models.CharField(max_length=50, verbose_name='Email')),
                ('Password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
    ]
