# Generated by Django 4.2.7 on 2023-11-02 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_published_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='description',
            new_name='brief',
        ),
    ]