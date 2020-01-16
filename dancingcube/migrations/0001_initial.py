# Generated by Django 3.0.2 on 2020-01-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('music', models.CharField(max_length=200)),
                ('difficulty', models.CharField(choices=[('1', 'easy'), ('2', 'medium'), ('3', 'hard')], default='1', max_length=1)),
                ('uploader', models.CharField(max_length=200)),
                ('map', models.FileField(upload_to='media/maps/')),
            ],
        ),
    ]