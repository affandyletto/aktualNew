from django.contrib import admin

from .models import talenta,kriteriaTalenta,tglKriteria,PhDP
from import_export.admin import ImportExportModelAdmin
@admin.register(talenta)
@admin.register(kriteriaTalenta)
@admin.register(tglKriteria)
@admin.register(PhDP)
class user(ImportExportModelAdmin):
	pass