# Generated by Django 3.2.23 on 2024-02-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWeb', '0021_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=None, max_length=255),
        ),
    ]