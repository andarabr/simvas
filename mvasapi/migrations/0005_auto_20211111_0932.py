# Generated by Django 3.2.8 on 2021-11-11 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvasapi', '0004_auto_20211108_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='http_status',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='last_post_try',
            field=models.DateTimeField(null=True),
        ),
    ]