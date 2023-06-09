# Generated by Django 4.2 on 2023-04-04 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='tarefas',
            field=models.ManyToManyField(to='tarefas.tarefa', verbose_name='Tarefas'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
