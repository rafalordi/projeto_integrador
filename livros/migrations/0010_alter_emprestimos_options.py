# Generated by Django 3.2.7 on 2021-10-13 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0009_rename_emprestimo_emprestimos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimos',
            options={'verbose_name': 'Emprestimo'},
        ),
    ]
