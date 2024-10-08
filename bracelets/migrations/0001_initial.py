# Generated by Django 3.1.14 on 2022-01-22 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bracelet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BraceletImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bracelet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='bracelets.bracelet')),
            ],
        ),
    ]
