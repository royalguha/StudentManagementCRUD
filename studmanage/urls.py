from django.urls import path
from .views import DataForm,DataListView,DataDeleteView,DataUpdateView,NameFilterView

from . import views


from django.views.generic import TemplateView


urlpatterns = [
    path('',DataForm.as_view(),name=""),
   # path("login", Login.as_view(), name="login"),
    path("suc/",TemplateView.as_view(template_name="suc.html")),
    path("kaka/",DataListView.as_view(),name="kaka"),
    path("<int:pk>/delete/",DataDeleteView.as_view(),name="delete"),
    path("<int:pk>/update",DataUpdateView.as_view(),name="update"),
    path("filter/",views.DatafilterView,name="filter"),
    path("filtername/",NameFilterView.as_view(),name="filtername")
]