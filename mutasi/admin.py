from django.contrib import admin

# Register your models here.
from .models import mutasi,plt,aps
from import_export.admin import ImportExportModelAdmin
@admin.register(mutasi)
@admin.register(plt)
@admin.register(aps)
class user(ImportExportModelAdmin):
	pass