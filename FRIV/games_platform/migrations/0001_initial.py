# Generated by Django 2.2.3 on 2019-07-23 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_platform.Game')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_platform.Player')),
            ],
        ),
    ]