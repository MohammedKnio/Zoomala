# Generated by Django 2.2 on 2020-05-02 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0005_auto_20200502_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='link',
            field=models.CharField(max_length=2000, verbose_name='link'),
        ),
    ]