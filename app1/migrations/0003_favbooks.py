# Generated by Django 4.1.4 on 2022-12-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_recommend_genre_alter_recommend_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=50, verbose_name='Enter Book Name')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]