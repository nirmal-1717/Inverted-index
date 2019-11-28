from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_board, name='dash_board'),
    path('next', views.next, name='next'),
    path('clear',views.clear, name='clear'),
    path('back',views.back, name='back')
]
