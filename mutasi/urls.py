from django.urls import path
from django.views.generic import ListView
from .views import pdf_aps,pdf_mutasi,pdf_plt,deletePLT,mutasiUpdate,delete,pltUpdate,mutasiCreate,pltCreate,mutasiView,pltView,apsView,apsUpdate,deleteAPS,apsCreate
from general.general import kirim,relod
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .models import plt,mutasi
from django.urls import re_path, include

app_name="mutasi"
urlpatterns = [
	path('', mutasiView.as_view(), name="index"),
	path('plt', pltView.as_view(), name="plt"),
	path('aps', apsView.as_view(), name="aps"),
	path('reload/<slug:template>', relod, name="relod"),
	path('kirim', kirim, name="kirim"),
	path("pdf/<slug:pk>", pdf_mutasi.as_view(), name="pdf"),
	path("pdf_plt/<slug:pk>", pdf_plt.as_view(), name="pdf_plt"),
	path("pdf_aps/<slug:pk>", pdf_aps.as_view(), name="pdf_aps"),
	path("edit/<slug:pk>", mutasiUpdate.as_view(), name="edit"),
	path("edit_plt/<slug:pk>", pltUpdate.as_view(), name="edit_plt"),
	path("edit_aps/<slug:pk>", apsUpdate.as_view(), name="edit_aps"),
	path("delete/<slug:pk>", delete, name="delete"),
	path("deleteAPS/<slug:pk>", deleteAPS, name="deleteAPS"),
	path("deletePLT/<slug:pk>", deletePLT, name="deletePLT"),
	path("tambah", mutasiCreate.as_view(), name="tambah"),
	path("tambah_plt", pltCreate.as_view(), name="tambah_plt"),
	path("tambah_aps", apsCreate.as_view(), name="tambah_aps"),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)