# Generated by Django 3.0 on 2019-12-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191212_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
