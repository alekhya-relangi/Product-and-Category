# Generated by Django 3.1.7 on 2021-06-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20210615_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='/'),
        ),
    ]
