# Generated by Django 3.1.14 on 2022-02-03 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracelets', '0007_item_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
