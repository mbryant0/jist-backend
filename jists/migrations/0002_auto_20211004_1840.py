# Generated by Django 3.2.7 on 2021-10-04 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='jists',
        ),
        migrations.AddField(
            model_name='jist',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jists.topic'),
        ),
    ]
