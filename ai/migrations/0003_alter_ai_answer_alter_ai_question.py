# Generated by Django 5.1.1 on 2025-02-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai", "0002_remove_ai_body_remove_ai_title_ai_answer_ai_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ai",
            name="answer",
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="ai",
            name="question",
            field=models.TextField(default=None, null=True),
        ),
    ]
