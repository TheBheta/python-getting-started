# Generated by Django 4.0.5 on 2022-06-19 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_game_alter_greeting_when'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
