# Generated by Django 3.2.5 on 2021-11-05 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blood_Group', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District_Name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Division_Name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(null=True, upload_to='profiles/')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Date_of_Birth', models.DateField()),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6, null=True)),
                ('Area', models.CharField(default='', max_length=20)),
                ('Postal_Code', models.IntegerField(default='')),
                ('last_donate_date', models.DateField()),
                ('any_disease', models.CharField(max_length=20)),
                ('Blood_Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blood', to='User.blood')),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district', to='User.district')),
                ('Division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='division', to='User.division')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
