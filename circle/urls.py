from django.urls import path
from . import views

app_name = 'circle'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-circle/', views.create_circle, name='create_circle'),
    path('join/<uuid:code>/', views.join, name='join'),
    path('score-confirm/<id>', views.score_confirm, name='score_confirm'),
    path('score-reject/<id>', views.score_reject, name='score_reject'),
]