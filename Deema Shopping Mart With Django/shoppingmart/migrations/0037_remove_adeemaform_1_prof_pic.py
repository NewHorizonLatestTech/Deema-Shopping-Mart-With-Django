# Generated by Django 4.1.3 on 2022-11-18 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shoppingmart", "0036_adeemaform_1_prof_pic"),
    ]

    operations = [
        migrations.RemoveField(model_name="adeemaform_1", name="prof_pic",),
    ]
