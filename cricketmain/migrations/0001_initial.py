# Generated by Django 2.2 on 2020-07-12 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=40)),
                ('logo_uri', models.URLField()),
                ('club_state', models.TextField(max_length=40)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricketmain.Team')),
            ],
            options={
                'db_table': 'point',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=40)),
                ('last_name', models.TextField(max_length=40)),
                ('image_uri', models.URLField(max_length=500)),
                ('jersey_number', models.IntegerField()),
                ('country', models.TextField(max_length=40)),
                ('history', models.TextField(max_length=500)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cricketmain.Team')),
            ],
            options={
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamone', to='cricketmain.Team')),
                ('teamtwo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamtwo', to='cricketmain.Team')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='cricketmain.Team')),
            ],
            options={
                'db_table': 'match',
            },
        ),
    ]
