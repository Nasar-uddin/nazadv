# Generated by Django 2.1.2 on 2020-04-29 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20200429_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category'),
        ),
    ]
