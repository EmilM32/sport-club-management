# Generated by Django 2.2.2 on 2019-06-15 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainlist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
