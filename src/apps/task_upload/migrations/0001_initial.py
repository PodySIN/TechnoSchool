# Generated by Django 5.1.4 on 2025-01-01 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Questions",
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
                ("Number", models.IntegerField(default=1)),
                ("Topic", models.CharField(default="Разное", max_length=512)),
            ],
            options={
                "db_table": "Questions",
            },
        ),
        migrations.CreateModel(
            name="SourceTasks",
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
                (
                    "Image",
                    models.ImageField(
                        default=None,
                        help_text="Изображение прилагаемое для выполнения задания.",
                        upload_to="task_images/",
                    ),
                ),
                ("Video", models.ImageField(default=None, upload_to="task_videos/")),
                (
                    "Solution",
                    models.ImageField(default=None, upload_to="task_solution/"),
                ),
                ("Number", models.IntegerField(default=1)),
                ("Topic", models.CharField(default="Разное", max_length=512)),
                ("Condition", models.CharField(default="", max_length=2048)),
                (
                    "Condition_for_students",
                    models.CharField(default="", max_length=2048),
                ),
                ("Answer", models.IntegerField(default=1)),
            ],
            options={
                "db_table": "SourceTasks",
            },
        ),
        migrations.CreateModel(
            name="PrototypeTasks",
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
                ("Image", models.ImageField(default=None, upload_to="task_images/")),
                ("Number", models.IntegerField(default=1)),
                ("Topic", models.CharField(default="Разное", max_length=512)),
                ("Condition", models.CharField(default="", max_length=2048)),
                ("Answer", models.FloatField(default=1.0)),
                (
                    "SourceTask",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="PrototypeTasks",
                        to="task_upload.sourcetasks",
                    ),
                ),
            ],
            options={
                "db_table": "PrototypeTasks",
            },
        ),
        migrations.CreateModel(
            name="Limitations",
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
                ("Limitation", models.CharField(default="", max_length=2048)),
                (
                    "Task",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="limitations",
                        to="task_upload.sourcetasks",
                    ),
                ),
            ],
            options={
                "db_table": "Limitations",
            },
        ),
        migrations.CreateModel(
            name="Formulas",
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
                ("Formula", models.CharField(default="", max_length=2048)),
                (
                    "Task",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="formulas",
                        to="task_upload.sourcetasks",
                    ),
                ),
            ],
            options={
                "db_table": "Formulas",
            },
        ),
        migrations.CreateModel(
            name="Topics",
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
                ("Topic", models.CharField(default="Разное", max_length=512)),
                (
                    "question",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="topics",
                        to="task_upload.questions",
                    ),
                ),
            ],
            options={
                "db_table": "Topics",
            },
        ),
    ]
