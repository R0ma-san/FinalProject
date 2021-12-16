# Generated by Django 3.2.9 on 2021-12-14 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Катерогия',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Специализация университета',
                'verbose_name_plural': 'Специализации университета',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название университета')),
                ('country', models.CharField(max_length=128, verbose_name='Страна расположения')),
                ('body', models.CharField(max_length=1000, verbose_name='Краткое описание')),
                ('images', models.ImageField(null=True, upload_to='', verbose_name='Фотография')),
                ('url', models.URLField(unique=True, verbose_name='Ссылка на официальный сайт')),
                ('deadline_ed', models.DateField(verbose_name='Окончание приема заявок на early decision')),
                ('deadline_rd', models.DateField(verbose_name='Окончание приема заявок regular decision')),
                ('TOEFL', models.PositiveSmallIntegerField(default=0, verbose_name='рекомендованый балл по TOEFL')),
                ('SAT', models.PositiveIntegerField(default=0, verbose_name='рекомендованый балл по SAT')),
                ('IELTS', models.FloatField(default=0, verbose_name='рекомендованый балл по IELTS')),
                ('GPA', models.FloatField(default=0, verbose_name='рекомендованый средний балл в школе ')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликованно')),
                ('price', models.PositiveIntegerField(default=0, verbose_name=' Цена обучения')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='university_category', to='universities.category', verbose_name='Направление обучения')),
                ('specialization', models.ManyToManyField(to='universities.Specialization', verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Университет',
                'verbose_name_plural': 'Университеты',
            },
        ),
    ]
