from django.urls import path
from .views import LogoutView, RegisterView,LoginView, UserView,RefreshToken

urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('user',UserView.as_view()),
    path('logout',LogoutView.as_view()),
    path('refresh',RefreshToken.as_view()),
    
]