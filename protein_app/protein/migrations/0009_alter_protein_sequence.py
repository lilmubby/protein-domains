# Generated by Django 4.0.4 on 2022-06-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0008_remove_protein_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protein',
            name='sequence',
            field=models.CharField(max_length=200),
        ),
    ]