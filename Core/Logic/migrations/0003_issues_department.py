# Generated by Django 3.2.8 on 2021-10-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logic', '0002_auto_20211028_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='issues',
            name='Department',
            field=models.CharField(choices=[('ADM', 'Administrator'), ('MGM', 'Management')], default='Admin', max_length=200),
        ),
    ]
