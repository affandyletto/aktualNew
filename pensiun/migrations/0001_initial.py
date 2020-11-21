# Generated by Django 3.0.7 on 2020-11-08 19:18

from django.db import migrations, models
import django.db.models.deletion
import pensiun.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pegawai', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pensiun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nipeg', models.CharField(default='', max_length=20)),
                ('file', models.FileField(blank=True, upload_to=pensiun.models.upload_location)),
                ('terkirim', models.BooleanField(default=False)),
                ('peg', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pegawai.pegawai')),
            ],
        ),
    ]