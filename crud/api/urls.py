from django.urls import path
from api import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.crudList, name="task-list"),
    path('task-create/', views.crudCreate, name="task-create"),
    path('task-detail/<str:pk>/', views.crudDetail, name="task-detail"),
    path('task-update/<str:pk>/', views.crudUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.crudDelete, name="task-delete"),
]
