# Generated by Django 4.0.4 on 2022-06-12 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0003_delete_protein_delete_taxa'),
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Domain',
        ),
        migrations.DeleteModel(
            name='Pfam',
        ),
    ]
