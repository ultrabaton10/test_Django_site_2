# Generated by Django 4.2.1 on 2023-06-14 03:46

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
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='C:\\Users\\gaming\\PycharmProjects\\test_Django_site_2\\test_project\\app1/media/app1', verbose_name='изображение')),
                ('name', models.CharField(max_length=50, verbose_name='название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='C:\\Users\\gaming\\PycharmProjects\\test_Django_site_2\\test_project\\app1/media/app1', verbose_name='изображение')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('author', models.CharField(max_length=50, verbose_name='автор')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]