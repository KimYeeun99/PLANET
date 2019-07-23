from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from rest_framework.decorators import api_view

from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from .utils import format_quote, get_user_model, get_username_field

from rest_framework import generics
from user.models import CustomerUser
import random
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@login_required
def inbox(request):
    if request.method == 'GET':
        message_list = Message.objects.inbox_for(request.user)
        serializer = MessageSerializer(message_list, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
def outbox(request):
    if request.method == 'GET':
        message_list = Message.objects.outbox_for(request.user)
        serializer = MessageSerializer(message_list, many = True)
    return Response(serializer.data)

class outbox_Detail(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class MessageCustom(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

     def perform_create(self,serializer):
        max_id = CustomerUser.objects.order_by('-id')[0].id
        for x in range(1,max_id+1):
            random_id = random.randint(1, max_id + 1)
            if random_id == queryset[sender]:
                continue
            else:
                random_object = CustomerUser.objects.filter(id__gte=random_id)[0]
                break
        
        while random_id == self.request.user.id:
            random_id = random.randint(1, max_id + 1)
            random_object = CustomerUser.objects.filter(id__gte=random_id)[0]
        serializer.save(sender=self.request.user,recipient=random_object
        
class MessageDetail(generics.RetrieveDestroyAPIView,generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        message = get_object_or_404(Message, pk=self.kwargs.get('pk'))
        serializer.save(sender=self.request.user,recipient=message.sender,parent_msg=message)