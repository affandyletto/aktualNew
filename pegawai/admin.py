from django.contrib import admin

# Register your models here.
from .models import pegawai
from import_export.admin import ImportExportModelAdmin
@admin.register(pegawai)
class user(ImportExportModelAdmin):
	pass