# Generated by Django 3.2.5 on 2021-11-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Blood_Group',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='District',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Division',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
