# Generated by Django 4.0.3 on 2022-03-24 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sc18y2h', '0002_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module_pro',
            name='score',
        ),
        migrations.CreateModel(
            name='module_pro_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='score')),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc18y2h.module', verbose_name='ID')),
                ('pro_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc18y2h.professors', verbose_name='pro_Name')),
            ],
        ),
    ]
