# Generated by Django 4.0.5 on 2022-06-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_guess_closest_alter_guess_guess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]