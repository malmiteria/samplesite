from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_view, name='create_view'),
    path('edit/<int:grid_id>', views.edit_grid, name='edit_grid'),
]
