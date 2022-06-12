from django.urls import path
from . import views

boosts = views.BoostViewSet.as_view({
    'get': 'list', # Получить список всех бустов
    'post': 'create', # Создать буст
})

lonely_boost = views.BoostViewSet.as_view({
    'put': 'partial_update', # редактировать буст
})

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('call_click/', views.call_click, name='call-click'),
    path('', views.index, name='index'),
    path('boost/<int:pk>/', lonely_boost, name='boost'),
    path('boosts/', boosts, name='boosts'),
    path('update_coins/', views.update_coins),
    path('core/', views.get_core)
]
