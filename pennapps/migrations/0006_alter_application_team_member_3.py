# Generated by Django 5.0.1 on 2024-02-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pennapps', '0005_alter_application_major_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='team_member_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
