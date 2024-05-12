# Generated by Django 5.0.1 on 2024-05-11 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0006_delete_checklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('done', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookmodule.task')),
            ],
        ),
    ]