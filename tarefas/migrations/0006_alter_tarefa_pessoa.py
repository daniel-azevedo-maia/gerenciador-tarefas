# Generated by Django 5.1.5 on 2025-01-21 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0005_remove_pessoa_tarefas_tarefa_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='pessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='tarefas.pessoa'),
        ),
    ]
