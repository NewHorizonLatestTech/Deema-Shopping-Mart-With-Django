# Generated by Django 4.1.3 on 2022-11-18 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shoppingmart", "0034_alter_adeemaform_1_datetime"),
    ]

    operations = [
        migrations.RemoveField(model_name="student_data", name="Dath_Of_Birth",),
    ]
