# Generated by Django 2.2.1 on 2019-07-30 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190729_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
