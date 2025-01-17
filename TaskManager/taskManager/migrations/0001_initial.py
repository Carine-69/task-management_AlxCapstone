# Generated by Django 5.1.4 on 2025-01-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taskManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Due_Date', models.DateTimeField(auto_now_add=True)),
                ('Priority_Level', models.PositiveIntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], default=1)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
    ]
