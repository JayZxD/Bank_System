# Generated by Django 3.2.7 on 2021-09-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='balance',
            field=models.IntegerField(default=14242141),
        ),
        migrations.AddField(
            model_name='users',
            name='contact_no',
            field=models.IntegerField(default=134142),
        ),
        migrations.AddField(
            model_name='users',
            name='email_id',
            field=models.EmailField(default=141412421, max_length=254),
        ),
    ]