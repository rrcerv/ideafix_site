# Generated by Django 4.2.4 on 2023-09-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='nivel_admin',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
