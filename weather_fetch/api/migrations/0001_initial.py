# Generated by Django 3.2.18 on 2023-04-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(max_length=12)),
                ('long', models.FloatField(max_length=12)),
                ('Date', models.DateField()),
            ],
        ),
    ]
