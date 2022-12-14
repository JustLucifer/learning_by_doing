# Generated by Django 4.0.6 on 2022-08-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_category_women_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['time_create', 'title'], 'verbose_name': 'Известные женщины', 'verbose_name_plural': 'Известные женщины'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='women',
            name='content',
            field=models.TextField(verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
    ]
