# Generated by Django 4.1.3 on 2022-11-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="pseudonym",
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
