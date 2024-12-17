# biotools/urls.py
from django.urls import path

from . import views

app_name = "biotools"  # This sets the namespace
urlpatterns = [
    path("seqcontent/", views.seqcontent_view, name="seqcontent"),
    path("revcomp/", views.revcomp_view, name="revcomp"),
    path("random_dna/", views.random_dna_view, name="random_dna"),
]
