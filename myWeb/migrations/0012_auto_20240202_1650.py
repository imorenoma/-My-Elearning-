# Generated by Django 3.2.23 on 2024-02-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWeb', '0011_user_confirmpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmPassword',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]