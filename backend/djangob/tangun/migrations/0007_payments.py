# Generated by Django 2.2.2 on 2019-06-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangun', '0006_mainlist_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(null=True)),
                ('month', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
    ]
