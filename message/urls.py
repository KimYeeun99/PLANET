from django.urls import include, path
from . import views
from .views import MessageCustom,MessageDetail,inbox_Detail,outbox_Detail

urlpatterns = [
    path('inbox/', views.inbox),
    #path('inbox/<int:pk>/',inbox_Detail.as_view()),
    path('outbox/', views.outbox),
    path('outbox/<int:pk>',outbox_Detail.as_view()),
    path('',MessageCustom.as_view()),
    path('inbox/<int:pk>',MessageDetail.as_view()),
]
