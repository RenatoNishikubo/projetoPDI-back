# Generated by Django 4.2.13 on 2024-05-24 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_alter_declarante_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dependente',
            old_name='declarante_id',
            new_name='declarante',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='declarante_id',
            new_name='declarante',
        ),
        migrations.RenameField(
            model_name='propriedade',
            old_name='declarante_id',
            new_name='declarante',
        ),
    ]
