from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ClientSerializer, MessageSerializer, MailingSerializer
from .models import Client, Mailing, Message


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

    @action(detail=True, methods=['get'])
    def info(self, request, pk=None):
        """
        Сводные данные по конкретной рассылке
        """
        queryset = Mailing.objects.all()
        mailing = get_object_or_404(queryset, pk=pk)
        serializer = MailingSerializer(mailing)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def fullinfo(self, request):
        """
        Сводные данные по всем рассылкам
        """
        queryset = Mailing.objects.all()
        serializer = MailingSerializer(queryset, many=True)
        return Response(serializer.data)

