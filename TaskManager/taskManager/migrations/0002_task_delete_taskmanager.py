# Generated by Django 5.1.4 on 2025-01-12 07:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Due_Date', models.DateTimeField(auto_now_add=True)),
                ('Priority_Level', models.PositiveIntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], default=1)),
                ('Status', models.CharField(choices=[('pending', 'pending'), ('In progress', 'In progress'), ('Completed', 'Completed')], default='pending', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='taskManager',
        ),
    ]
