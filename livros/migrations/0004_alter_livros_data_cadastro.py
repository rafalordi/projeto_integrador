# Generated by Django 3.2.7 on 2021-09-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_alter_livros_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
