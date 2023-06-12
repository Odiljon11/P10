# Generated by Django 4.2.1 on 2023-05-24 21:03

from django.db import migrations, models
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_verificationcode'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(max_length=129, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('supervisor', 'Supervisor')], default='student', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
