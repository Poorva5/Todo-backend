# Generated by Django 4.1.2 on 2022-11-02 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0002_alter_taskdata_created_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="taskdata",
            old_name="created_by",
            new_name="user",
        ),
    ]
