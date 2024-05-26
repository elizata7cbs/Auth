
from django.contrib import admin
from django.urls import path, include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # path('', views.index),
    path('add_task/', views.add_task),
    path('register/', views.register_user),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
