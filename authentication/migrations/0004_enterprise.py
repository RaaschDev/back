# Generated by Django 3.2.6 on 2021-08-19 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210819_0451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='authentication.profile')),
            ],
        ),
    ]