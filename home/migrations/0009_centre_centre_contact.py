# Generated by Django 3.0.5 on 2020-04-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200419_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='centre',
            name='centre_contact',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
