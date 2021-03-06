# -*- coding: utf-8 -*-
from .models import Event, EventType, Reporter
from .serializers import (
    EventSerializer, ReporterSerializer, EventTypeSerializer)
from .pagination_classes import DefaultEdgarPagination

from django.shortcuts import get_object_or_404
from rest_framework import generics


# Create your views here.
class events_list(generics.ListAPIView):
    """Endpoint to list events"""
    serializer_class = EventSerializer
    pagination_class = DefaultEdgarPagination

    def get_queryset(self):
        return Event.objects.all()

    def filter_queryset(self, queryset):
        uuid = self.request.query_params.get('uuid', None)
        name = self.request.query_params.get('name', None)
        location = self.request.query_params.get('location', None)
        if uuid and len(uuid) > 0:
            queryset = queryset.filter(uuid__icontains=uuid)
        if name and len(name) > 0:
            queryset = queryset.filter(name__icontains=name)
        if location and len(location) > 0:
            queryset = queryset.filter(location__icontains=location)
        return queryset


class event_detail(generics.RetrieveAPIView):
    """Returns the detail of a single event"""
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()


class reporters_list(generics.ListAPIView):
    """Returns all reporters paginated"""
    serializer_class = ReporterSerializer
    pagination_class = DefaultEdgarPagination

    def get_queryset(self):
        return Reporter.objects.all()

    def filter_queryset(self, queryset):
        name = self.request.query_params.get('name', None)
        id = self.request.query_params.get('id', None)
        if name and len(name) > 0:
            queryset = queryset.filter(name__icontains=name)
        if id and len(id) > 0:
            queryset = queryset.filter(id__contains=id)
        return queryset


class reporter_events(generics.ListAPIView):
    """Returns the list of a reporter events using the reporter ID as filter key"""
    serializer_class = EventSerializer
    pagination_class = DefaultEdgarPagination

    def get_queryset(self):
        reporter = get_object_or_404(Reporter, pk=self.kwargs['reporter_id'])
        return Event.objects.filter(reporter=reporter)


class types_list(generics.ListAPIView):
    """Returns the list of all the event types"""
    serializer_class = EventTypeSerializer
    pagination_class = DefaultEdgarPagination

    def get_queryset(self):
        return EventType.objects.all()

    def filter_queryset(self, queryset):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        if id and len(id) > 0:
            queryset = queryset.filter(id__contains=id)
        if name and len(name) > 0:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class events_per_type(generics.ListAPIView):
    """Returns the list of events per type using the type ID as filter key"""
    serializer_class = EventSerializer
    pagination_classes = DefaultEdgarPagination

    def get_queryset(self):
        type_id = self.kwargs['type_id']
        type = get_object_or_404(EventType, id=type_id)
        return Event.objects.filter(event_type=type)
