# Generated by Django 4.1.3 on 2022-11-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shoppingmart", "0035_remove_student_data_dath_of_birth"),
    ]

    operations = [
        migrations.AddField(
            model_name="adeemaform_1",
            name="prof_pic",
            field=models.ImageField(
                default="", max_length=50, upload_to="profile_pics"
            ),
        ),
    ]
