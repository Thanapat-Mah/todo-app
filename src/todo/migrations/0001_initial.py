# Generated by Django 4.0 on 2021-12-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('is_complete', models.BooleanField(default=False)),
                ('due_datetime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
