# Generated by Django 4.1.5 on 2023-02-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0002_profession_student_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Write details/description about your self. Like you can also describe your past experiences as well', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='static/images/user.png', upload_to='Profile/images'),
        ),
    ]
