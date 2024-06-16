# Generated by Django 5.0.6 on 2024-06-16 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleId', models.BigIntegerField()),
                ('accountEmail', models.EmailField(max_length=254)),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topics', to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('markdown', models.TextField()),
                ('learning', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modules', to='courses.course')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modules', to='courses.topic')),
            ],
        ),
    ]