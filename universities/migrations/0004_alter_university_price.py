# Generated by Django 3.2.9 on 2021-12-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0003_alter_university_top_worldwide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name=' Стоимость обучения с проживанием'),
        ),
    ]
