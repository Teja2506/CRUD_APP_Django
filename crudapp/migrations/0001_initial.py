# Generated by Django 3.2.19 on 2023-08-04 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_no', models.IntegerField()),
                ('Name', models.CharField(max_length=20)),
                ('Qualification', models.CharField(max_length=20)),
                ('Course_joied', models.CharField(max_length=20)),
            ],
        ),
    ]
