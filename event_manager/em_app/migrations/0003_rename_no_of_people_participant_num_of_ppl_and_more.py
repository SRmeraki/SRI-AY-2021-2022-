# Generated by Django 4.0.1 on 2022-01-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('em_app', '0002_alter_participant_registration_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='no_of_people',
            new_name='num_of_ppl',
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='participant',
            name='registration_type',
            field=models.CharField(choices=[('SING', 'INDIVIDUAL'), ('GRP', 'GROUP')], max_length=50),
        ),
    ]