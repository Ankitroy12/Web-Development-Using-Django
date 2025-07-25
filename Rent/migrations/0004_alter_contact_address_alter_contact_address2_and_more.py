# Generated by Django 5.1.3 on 2024-12-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0003_contact_address_contact_address2_contact_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
