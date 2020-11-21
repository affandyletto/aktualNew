from django.contrib import admin

# Register your models here.
from .models import pensiun
from import_export.admin import ImportExportModelAdmin
@admin.register(pensiun)
class user(ImportExportModelAdmin):
	pass