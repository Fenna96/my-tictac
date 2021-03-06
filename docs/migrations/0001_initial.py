# Generated by Django 3.2 on 2021-05-02 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicRoom',
            fields=[
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Stanza base',
                'verbose_name_plural': 'Stanze base',
                'db_table': 'docs_basic_room',
            },
        ),
        migrations.CreateModel(
            name='BasicPosition',
            fields=[
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('immagine', models.FileField(blank=True, null=True, upload_to='')),
                ('dettaglio', models.JSONField(default=dict)),
                ('stanza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='docs.basicroom')),
            ],
            options={
                'verbose_name': 'Posizione base',
                'verbose_name_plural': 'Posizione base',
                'db_table': 'docs_basic_position',
            },
        ),
        migrations.CreateModel(
            name='BasicDoc',
            fields=[
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_documento', models.DateField(blank=True, null=True)),
                ('posizione', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='docs.basicposition')),
            ],
            options={
                'verbose_name': 'Documento base',
                'verbose_name_plural': 'Documento base',
                'db_table': 'docs_basic_doc',
            },
        ),
    ]
