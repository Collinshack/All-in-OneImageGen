# Generated by Django 4.2.1 on 2023-05-16 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_waitlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlist',
            name='more_features',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
