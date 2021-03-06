# Generated by Django 2.0.13 on 2019-12-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda_text', models.CharField(max_length=200)),
                ('agenda_detail', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
