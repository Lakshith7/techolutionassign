# Generated by Django 3.2.9 on 2021-11-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=100)),
                ('objectname', models.CharField(max_length=100)),
            ],
        ),
    ]
