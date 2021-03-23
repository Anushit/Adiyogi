# Generated by Django 3.1.4 on 2021-03-16 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_employee_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('shortdescription', models.TextField(max_length=100)),
                ('longdescription', models.TextField(max_length=100)),
                ('metatitle', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img/')),
            ],
        ),
    ]
