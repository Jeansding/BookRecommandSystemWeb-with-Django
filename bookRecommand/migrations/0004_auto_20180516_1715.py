# Generated by Django 2.0.5 on 2018-05-16 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookRecommand', '0003_auto_20180516_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='index',
            new_name='bookIndex',
        ),
    ]
