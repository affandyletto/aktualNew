# Generated by Django 3.0.7 on 2020-11-08 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pegawai', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tglKriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tgl2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tgl3', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tgl4', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tgl5', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tgl6', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tgl7', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tgl8', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('posisi', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='talenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(default=1)),
                ('nipeg', models.CharField(default='', max_length=50)),
                ('nama', models.CharField(default='', max_length=100)),
                ('jenjangMayoritas', models.CharField(default='', max_length=255)),
                ('jabatanSekarang', models.CharField(default='', max_length=255)),
                ('jenjangSebelum', models.CharField(default='', max_length=255)),
                ('gradeSebelum', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('skalaGajiSebelum', models.CharField(default='', max_length=100)),
                ('tglGrade', models.CharField(default='', max_length=100)),
                ('g1', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('g2', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('g3', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('g4', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('g5', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('g6', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('g7', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('g8', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('jenjangSesudah', models.CharField(default='', max_length=30)),
                ('gradeSesudah', models.CharField(default='', max_length=30)),
                ('skalaGajiSesudah', models.CharField(default='', max_length=30)),
                ('tglNaik', models.CharField(default='', max_length=30)),
                ('naikPer', models.CharField(default='', max_length=30)),
                ('keterangan', models.CharField(default='', max_length=80)),
                ('noSk', models.CharField(default='', max_length=100)),
                ('tglSkKenaikan', models.CharField(default='', max_length=30)),
                ('noSkNaik', models.CharField(default='', max_length=30)),
                ('tglPeriode', models.CharField(default='', max_length=100)),
                ('tglBerlaku', models.CharField(default='', max_length=100)),
                ('terkirim', models.BooleanField(default=False)),
                ('peg', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pegawai.pegawai')),
            ],
        ),
        migrations.CreateModel(
            name='PhDP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(default=1)),
                ('nipeg', models.CharField(default='', max_length=50)),
                ('periode', models.CharField(default='', max_length=100)),
                ('nama', models.CharField(default='', max_length=100)),
                ('grade', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('skalaLama', models.CharField(default='', max_length=100)),
                ('skalaBaru', models.CharField(default='', max_length=100)),
                ('noSk', models.CharField(default='', max_length=100)),
                ('tglBerlaku', models.CharField(default='', max_length=100)),
                ('tglSk', models.CharField(default='', max_length=100)),
                ('terkirim', models.BooleanField(default=False)),
                ('peg', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pegawai.pegawai')),
            ],
        ),
        migrations.CreateModel(
            name='kriteriaTalenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(default=1)),
                ('nipeg', models.CharField(default='', max_length=50)),
                ('nama', models.CharField(default='', max_length=100)),
                ('grade', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('g1', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('g2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('g3', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('g4', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('g5', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('g6', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('g7', models.CharField(blank=True, default='', max_length=2005, null=True)),
                ('g8', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('noSk', models.CharField(default='', max_length=100)),
                ('tglSk', models.CharField(default='', max_length=100)),
                ('tglBerlaku', models.CharField(default='', max_length=100)),
                ('tglPeriode', models.CharField(default='', max_length=100)),
                ('terkirim', models.BooleanField(default=False)),
                ('peg', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pegawai.pegawai')),
            ],
        ),
    ]