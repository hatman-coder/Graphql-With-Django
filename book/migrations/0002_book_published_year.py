# Generated by Django 4.2.7 on 2023-11-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
