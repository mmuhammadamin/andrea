# Generated by Django 4.0.5 on 2022-06-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_single',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
