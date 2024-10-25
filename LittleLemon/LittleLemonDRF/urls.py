from django.urls import path
from . import views

urlpatterns = [
    path('catagories', views.CategoriesViews.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
]