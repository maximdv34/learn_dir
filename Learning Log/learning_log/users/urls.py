
from django.urls import path, include
from . import views

urlpatterns = [
    # path('login/', views.login_, name='login')
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('login/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout')
]
