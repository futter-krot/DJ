# Generated by Django 2.2.6 on 2021-03-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20210321_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redaction',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
