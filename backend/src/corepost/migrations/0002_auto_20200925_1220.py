# Generated by Django 2.2.6 on 2020-09-25 12:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('corepost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
