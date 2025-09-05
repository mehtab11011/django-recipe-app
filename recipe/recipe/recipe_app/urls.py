
from django.contrib import admin
from django.urls import path ,include
from recipe_app import views
urlpatterns = [
    path("add_recipe/",views.add_view,name="home_page"),
    path("success_page/",views.success_page,name="success_page"),
    path("view_recipe_page/",views.view_recipe_page,name="view_recipe_page"),
    path("detail_page/<int:pk>/",views.detail_page,name="detail_page"),
    path("home_page/",views.home_page,name="home_page_buttons"),
    
    
       
]
