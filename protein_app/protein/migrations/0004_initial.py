# Generated by Django 4.0.4 on 2022-06-12 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('domain', '0003_initial'),
        ('protein', '0003_delete_protein_delete_taxa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taxa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxa_id', models.CharField(max_length=10, unique=True)),
                ('clade', models.CharField(max_length=1)),
                ('genus', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein_id', models.CharField(max_length=20)),
                ('sequence', models.CharField(max_length=20)),
                ('length', models.IntegerField(default=0)),
                ('domains', models.ManyToManyField(to='domain.domain')),
                ('taxonomy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='protein.taxa')),
            ],
        ),
    ]