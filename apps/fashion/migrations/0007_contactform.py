# Generated by Django 4.0.5 on 2022-06-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0006_comment1'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]
