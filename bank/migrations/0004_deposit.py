# Generated by Django 3.2.7 on 2021-09-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20210911_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254)),
                ('contact_no', models.IntegerField()),
                ('amount', models.IntegerField(verbose_name='Amount (₹)')),
            ],
        ),
    ]
