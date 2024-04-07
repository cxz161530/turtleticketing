from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('turtles/', views.turtles_index, name="index"),
    path('turtles/<int:turtle_id>/', views.turtles_detail, name="detail"),
    path('turtles/create/', views.TurtleCreate.as_view(), name='turtles_create'),
    path('turtles/<int:pk>/update/', views.TurtleUpdate.as_view(), name='turtles_update'),
    path('turtles/<int:pk>/delete/', views.TurtleDelete.as_view(), name='turtles_delete'),
    path('turtles/<int:turtle_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('turtles/<int:turtle_id>/assoc_rock/<int:rock_id>/', views.assoc_rock, name='assoc_rock'),
    path('rocks/', views.RockList.as_view(), name='rocks_index'),
    path('rocks/<int:pk>/', views.RockDetail.as_view(), name='rocks_detail'),
    path('rocks/create/', views.RockCreate.as_view(), name='rocks_create'),
    path('rocks/<int:pk>/update/', views.RockUpdate.as_view(), name='rocks_update'),
    path('rocks/<int:pk>/delete/', views.RockDelete.as_view(), name='rocks_delete'),
]
