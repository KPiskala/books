# Generated by Django 3.2.5 on 2021-08-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.TextField(max_length=400)),
                ('author', models.TextField(max_length=400)),
                ('publication_date', models.DateField()),
                ('isbn', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('pages', models.IntegerField(null=True)),
                ('link', models.TextField(max_length=400, null=True)),
                ('language', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
