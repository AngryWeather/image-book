# Generated by Django 4.2.5 on 2023-10-15 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='date',
            new_name='date_posted',
        ),
    ]
