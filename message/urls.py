from django.urls import include, path
from . import views
from .views import MessageCustom,MessageDetail,outbox_Detail

urlpatterns = [
    path('inbox/', views.inbox),
    path('outbox/', views.outbox),
    path('outbox/<int:pk>',outbox_Detail.as_view()),
    path('',MessageCustom.as_view()),
    path('inbox/<int:pk>',MessageDetail.as_view()),
]
