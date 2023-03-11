# Generated by Django 4.1.7 on 2023-03-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_post_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("DF", "Draft"), ("PB", "Published")],
                default="DF",
                max_length=2,
            ),
        ),
    ]
