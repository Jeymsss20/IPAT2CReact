# Generated by Django 5.0.4 on 2024-07-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_item_age_item_birth_date_item_birth_place_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='cizizenship',
        ),
        migrations.AddField(
            model_name='item',
            name='citizenship',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
