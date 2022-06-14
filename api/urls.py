from django.urls import path
from .views import *

urlpatterns = [
    # path('',views.apiOverview,name='api-overview'),
    # path('task-list/',views.taskList,name='task-list'),
    # path('task-detail/<str:pk>/',views.taskDetail,name='task-detail'),
    path('task-create/',taskCreate.as_view(),name='task-create'),
    # path('task-update/<str:pk>',views.taskUpdate,name='task-update'),
    # path('task-delete/<str:pk>',views.taskDelete,name='task-delete'),
]
