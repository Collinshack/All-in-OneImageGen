# Generated by Django 4.2.1 on 2023-05-12 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_image_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
