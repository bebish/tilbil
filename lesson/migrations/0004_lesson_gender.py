# Generated by Django 5.0.2 on 2024-06-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_lessoncategory_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], default='M', max_length=1),
        ),
    ]
