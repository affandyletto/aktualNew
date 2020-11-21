from django.urls import path
from django.views.generic import ListView
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from general.general import kirim,relod

app_name="talenta"
urlpatterns = [
	path('', talentaView.as_view(), name="index"),
	path('PhDP', PhDPView.as_view(), name="PhDP"),
	path('kriteria', kriteriaTalentaView.as_view(), name="kriteria"),
	path('reload/<slug:template>', relod, name="relod"),
	path('kirim', kirim, name="kirim"),
	path("pdf/<slug:pk>", PDFTemplateView.as_view(), name="pdf"),
	path("pdf_PhDP/<slug:pk>", PDFPhDP.as_view(), name="PDFPhDP"),
	path("pdfKriteria/<slug:pk>", PDFKriteria.as_view(), name="PDFKriteria"),
	path("edit/<slug:pk>", talentaUpdate.as_view(), name="edit"),
	path("kriteriaEdit/<slug:pk>", kriteriaUpdate.as_view(), name="kriteriaEdit"),
	path("phdpUpdate/<slug:pk>", phdpUpdate.as_view(), name="phdpUpdate"),
	path("delete/<slug:pk>", delete, name="delete"),
	path("kriteriaDelete/<slug:pk>", kriteriaDelete, name="kriteriaDelete"),
	path("phdpDelete/<slug:pk>", phdpDelete, name="phdpDelete"),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)