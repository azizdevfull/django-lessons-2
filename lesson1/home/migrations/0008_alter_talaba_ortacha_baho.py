# Generated by Django 4.1.7 on 2023-03-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_alter_talaba_guruh_raqami"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talaba",
            name="ortacha_baho",
            field=models.IntegerField(),
        ),
    ]
