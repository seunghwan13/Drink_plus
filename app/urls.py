from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search/', views.question_list, name='paging'),
    path('search/<pk>/', views.description, name='description'),

]
