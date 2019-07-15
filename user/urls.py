from django.urls import include, path
from .views import RegisterView, UserDetailView, CustomLogin

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
    path('login/', CustomLogin.as_view()),
]