# Generated by Django 4.2.7 on 2023-11-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0006_remove_fads_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='fads',
            name='name',
            field=models.CharField(default='no name', max_length=100),
        ),
    ]
