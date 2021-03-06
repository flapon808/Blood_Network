# Generated by Django 3.2.5 on 2021-11-06 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0007_auto_20211106_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloodbank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blood_Bank_Name', models.CharField(max_length=69)),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('RBC', 'RBC'), ('Plasma', 'Plasma'), ('Platelet', 'Platelet')], max_length=9, null=True)),
                ('price_per_bag', models.IntegerField(null=True)),
                ('Quantity', models.IntegerField(null=True)),
                ('Exipration_date', models.DateField()),
                ('Blood_Bank_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbank.bloodbank')),
                ('Blood_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bloodtype', to='User.blood')),
            ],
        ),
    ]
