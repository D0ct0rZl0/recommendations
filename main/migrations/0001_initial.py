# Generated by Django 2.1.2 on 2019-03-06 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('courses', models.ManyToManyField(related_name='courses', through='main.Choice', to='main.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(related_name='users', through='main.Choice', to='main.User'),
        ),
        migrations.AddField(
            model_name='choice',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='main.Course'),
        ),
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='main.User'),
        ),
    ]
