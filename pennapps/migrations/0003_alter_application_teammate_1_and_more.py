# Generated by Django 5.0.1 on 2024-02-08 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pennapps', '0002_application_birthday_application_is_first_hack_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='teammate_1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='teammate_2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='teammate_3',
            field=models.CharField(max_length=255, null=True),
        ),
    ]