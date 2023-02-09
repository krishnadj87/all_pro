# Generated by Django 4.1.5 on 2023-02-08 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('salary', models.PositiveIntegerField()),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='Employee/images')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees_app.department')),
            ],
        ),
    ]
