# Generated by Django 3.2.7 on 2021-10-03 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0005_auto_20210911_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_emprestimo',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='nome_emprestado',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='tempo_duracao',
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emprestado', models.CharField(blank=True, max_length=30)),
                ('data_emprestimo', models.DateField(blank=True, null=True)),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('tempo_duracao', models.DateField(blank=True, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livros.livros')),
            ],
        ),
    ]
