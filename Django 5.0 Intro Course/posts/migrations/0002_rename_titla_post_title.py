# Generated by Django 5.1.4 on 2024-12-17 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titla',
            new_name='title',
        ),
    ]
