# Generated by Django 4.0.5 on 2022-06-20 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_game_winner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('chat_id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=255)),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.game')),
            ],
        ),
    ]