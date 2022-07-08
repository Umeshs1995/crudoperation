from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.addStudent,name='add'),
    path('studlist/',views.studList,name='studlist'),
    path('delete/<int:id>/',views.deleteStud),
    path('edit/<int:id>/', views.updateStud),
]