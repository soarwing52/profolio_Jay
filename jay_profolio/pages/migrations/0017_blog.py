# Generated by Django 2.2.4 on 2019-08-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_education_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('link', models.URLField()),
                ('image', models.CharField(max_length=50)),
            ],
        ),
    ]
