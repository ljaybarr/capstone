# Generated by Django 5.0.7 on 2024-08-09 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_rename_expenses_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='budget.project'),
        ),
    ]
