# Generated by Django 3.0.2 on 2020-01-30 15:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0003_auto_20200130_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name=django.core.validators.MinValueValidator(0))),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('from_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_category', to='category.Category')),
                ('to_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_category', to='category.Category')),
            ],
            options={
                'db_table': 'tbl_operation',
            },
        ),
    ]
