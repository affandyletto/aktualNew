from django.urls import path
from django.views.generic.base import TemplateView
from .views import pegawaiView,pegawaiUpdate,delete,pegawaiCreate,hapusPegawai

app_name="pegawai"
urlpatterns = [
	path('',pegawaiView.as_view(),name="index"),
	path("edit/<slug:pk>", pegawaiUpdate.as_view(), name="edit"),
	path("delete/<slug:pk>", delete, name="delete"),
	path("hapusPegawai",hapusPegawai,name='hapusPegawai'),
	path("tambah", pegawaiCreate.as_view(), name="tambah"),
]