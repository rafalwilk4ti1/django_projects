# Generated by Django 3.2.6 on 2021-09-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0026_alter_client_phone_cell'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='amount_car',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
