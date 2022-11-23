# Generated by Django 4.1.3 on 2022-11-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "shoppingmart",
            "0038_delete_adeemaform_1_rename_email_student_data_desc_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("num", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("desc", models.CharField(max_length=50)),
                ("images", models.ImageField(default="", upload_to="image")),
            ],
        ),
        migrations.DeleteModel(name="Student_Data",),
    ]
