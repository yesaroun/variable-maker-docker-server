# Generated by Django 4.2 on 2023-04-20 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("variable_abbreviation", "0002_rename_variable_variables_serached_variable"),
    ]

    operations = [
        migrations.RenameField(
            model_name="variables",
            old_name="serached_variable",
            new_name="searched_variable",
        ),
    ]
