# Generated by Django 3.1.1 on 2020-09-12 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poem_gen', '0004_auto_20200912_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
