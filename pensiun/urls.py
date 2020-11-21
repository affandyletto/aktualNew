from django.urls import path
from django.views.generic.base import TemplateView
from .views import pensiunView,kirim,pensiunUpdate,delete,tambah
from general.general import relod

app_name="pensiun"
urlpatterns = [
	path('',pensiunView.as_view(),name="index"),
	path('kirim', kirim, name="kirim"),	
	path("edit/<slug:pk>", pensiunUpdate.as_view(), name="edit"),
	path("delete/<slug:pk>", delete, name="delete"),	
	path("tambah", tambah, name="tambah"),
	path('reload/<slug:template>', relod, name="relod"),
]