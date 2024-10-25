from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoriesViews.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
]