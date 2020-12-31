from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    #lookup_field = 'id'

    @action(detail=True, methods=["get"])
    def choices(self, *args, **kwargs):
        question = self.get_object()
        choices = Choice.objects.filter(questions=question)
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["post"])
    def choice(self, request, *args, **kwargs):
        data = request.data
        serializer = ChoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Deleted successfully", status=200)

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'partial_update':
            return QuestionPartialUpdateSerializer
        else:
            if self.action == 'retrieve':
                self.serializer_class.Meta.depth = 1
            else:
                self.serializer_class.Meta.depth = 0
            return self.serializer_class


class QuestionUpdateAPIView(UpdateAPIView):
    serializer_class = QuestionSerializer1
    queryset = Question.objects.all()


class ChoiceListViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            self.serializer_class.Meta.depth = 1
        else:
            self.serializer_class.Meta.depth = 0
        return self.serializer_class

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        result = {"detail": "Deleted successfully"}
        return Response(result, status=200)



class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return AnswerSerializer
        else:
            if self.action == 'retrieve':
                self.serializer_class.Meta.depth = 2
            else:
                self.serializer_class.Meta.depth = 1
            return self.serializer_class

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        result = {"detail": "Deleted successfully"}
        return Response(result, status=200)

    """def get_queryset(self):
        choice = Choice.objects.filter(choice_text=self.kwargs['id'])
        return choice"""

    """def create(self, request, choice_id=None):
        try:
            quiz = Choice.objects.get(choice__id=choice_id)
        except Choice.DoesNotExist:
            raise Http404
        serializer = QuestionSerializer(quiz.question.all(), many=True)
        return Response(serializer.data)"""

    """def create(self, request, id, choice_id):
        data=request.data
        data['question']
        data = {'choice': choice_id, 'question': id}
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            quiz = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""



