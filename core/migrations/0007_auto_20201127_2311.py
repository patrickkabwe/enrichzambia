# Generated by Django 3.1.2 on 2020-11-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_category_cat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_type',
            field=models.CharField(choices=[('Food', 'Food'), ('Electronic', 'Electronic'), ('Home Appreance', 'Home Appreance'), ('Clothing', 'Clothing'), ('Shoes', 'Shoes')], max_length=50),
        ),
    ]
