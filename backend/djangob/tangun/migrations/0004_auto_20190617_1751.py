# Generated by Django 2.2.2 on 2019-06-17 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tangun', '0003_auto_20190615_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('kup', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='playerkup',
            name='kup',
        ),
        migrations.RemoveField(
            model_name='playerkup',
            name='player_id',
        ),
        migrations.DeleteModel(
            name='Kup',
        ),
        migrations.DeleteModel(
            name='PlayerKup',
        ),
        migrations.AddField(
            model_name='mainlist',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tangun.Level'),
        ),
    ]
