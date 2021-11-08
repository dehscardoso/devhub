# Generated by Django 3.2.8 on 2021-11-04 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20211103_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('up', 'Like'), ('down', 'Dislike')], max_length=200),
        ),
    ]
