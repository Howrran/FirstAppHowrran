# Generated by Django 3.0.2 on 2020-01-31 15:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0003_auto_20200130_1550'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('user_id', 'name')},
        ),
    ]
