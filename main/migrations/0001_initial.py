# Generated by Django 3.2 on 2022-02-27 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='slotdb',
            fields=[
                ('slotid', models.BigAutoField(primary_key=True, serialize=False)),
                ('slot', models.DateTimeField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bookingdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.CharField(max_length=1)),
                ('slotid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.slotdb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
