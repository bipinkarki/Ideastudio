from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('panel/<str:pk>/', views.panel, name='panel'),
    path('/create-panel/', views.createPanel, name='create-panel'),
    path('/update-panel/<str:pk>/', views.updatePanel, name='update-panel'),
    path('/delete-panel/<str:pk>/', views.deletePanel, name='delete-panel'),
]
