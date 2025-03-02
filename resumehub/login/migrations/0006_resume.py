# Generated by Django 4.0.1 on 2023-04-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_delete_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
                ('workexp', models.CharField(max_length=100)),
                ('dins', models.CharField(max_length=50)),
                ('d1y', models.IntegerField()),
                ('d2y', models.IntegerField()),
                ('iins', models.CharField(max_length=50)),
                ('i1y', models.IntegerField()),
                ('i2y', models.IntegerField()),
                ('sins', models.CharField(max_length=50)),
                ('s1y', models.IntegerField()),
                ('s2y', models.IntegerField()),
                ('skills', models.CharField(max_length=100)),
                ('certifications', models.CharField(max_length=100)),
                ('achievements', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'resume',
            },
        ),
    ]
