# Generated by Django 5.2.3 on 2025-06-29 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptodo', '0002_remove_todotask_user_id_todotask_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotask',
            name='username',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
