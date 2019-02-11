from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/create', views.new_show),
    path('shows/<int:id>', views.show),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/update', views.edit),
    path('shows/<int:id>/destroy', views.delete)
]