# Generated by Django 5.1.2 on 2024-11-04 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_category_options_post_date_publish"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="is_public",
            field=models.BooleanField(default=True),
        ),
    ]
