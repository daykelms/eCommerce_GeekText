# Generated by Django 2.1.5 on 2019-02-04 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
