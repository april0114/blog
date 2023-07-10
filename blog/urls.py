from django.urls import path
from . import views
app_name ='blog'

urlpatterns =[
    path('index/',views.index, name = "index"),
    path('base/<spk>', views.base, name = "base" ),
    path('blogs_form/', views.blogs_form, name = "blogs_form"),
    path('delete/<int:spk>/', views.delete, name='delete'),
    path('blogs_update/<int:spk>/', views.blogs_update, name='blogs_update'),
]