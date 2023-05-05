# Generated by Django 4.1.7 on 2023-03-11 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=40)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('last_statusUpdate_date', models.DateTimeField()),
                ('host_commented', models.BooleanField(default=False)),
                ('guest_commented', models.BooleanField(default=False)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revs', to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revs', to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='Ntf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
                ('if_read', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ntfs', to=settings.AUTH_USER_MODEL)),
                ('rev', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ntfs', to='revs.rev')),
            ],
        ),
    ]
