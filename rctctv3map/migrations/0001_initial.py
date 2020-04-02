# Generated by Django 2.2.11 on 2020-04-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('v2_concept_id', models.CharField(db_index=True, max_length=5)),
                ('v2_term_id', models.CharField(db_index=True, max_length=2)),
                ('ctv3_term_id', models.CharField(db_index=True, max_length=5)),
                ('ctv3_termtyp', models.CharField(max_length=1)),
                ('ctv3_concept_id', models.CharField(db_index=True, max_length=5)),
                ('use_ctv3_term_id', models.CharField(db_index=True, max_length=5)),
                ('stat', models.CharField(max_length=1)),
                ('map_typ', models.CharField(max_length=3)),
                ('map_status', models.BooleanField()),
                ('effective_date', models.DateField()),
                ('is_assured', models.BooleanField()),
            ],
        ),
    ]
