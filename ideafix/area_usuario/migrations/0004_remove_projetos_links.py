# Generated by Django 4.2.4 on 2023-09-18 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area_usuario', '0003_rename_links_links_projetos_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetos',
            name='links',
        ),
    ]