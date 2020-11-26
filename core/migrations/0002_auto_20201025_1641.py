# Generated by Django 3.1.2 on 2020-10-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(choices=[('Mwaiseni', 'Mwaiseni'), ('Kadyonko', 'Kadyonko'), ('Mukolwe', 'Mukolwe')], default='Mwaisenis', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='deliver',
            field=models.CharField(blank=True, choices=[('', 'Do you Deliver?'), ('Y', 'Yes'), ('N', 'No')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(max_length=300),
        ),
    ]
