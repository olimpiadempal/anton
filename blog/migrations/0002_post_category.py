# Generated by Django 2.0.13 on 2020-06-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('Essen', 'Essen'), ('Körper', 'Körper'), ('Lifestyle', 'Lifestyle'), ('Sport', 'Sport'), ('Anders', 'Anders')], max_length=20),
        ),
    ]
