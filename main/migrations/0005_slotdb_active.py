# Generated by Django 3.2 on 2022-02-27 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220227_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='slotdb',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
