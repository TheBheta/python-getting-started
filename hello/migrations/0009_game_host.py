# Generated by Django 4.0.5 on 2022-06-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='host',
            field=models.CharField(default='', max_length=100),
        ),
    ]
