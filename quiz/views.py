from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import QuestionSerializer, ChoiceSerializer, AnswerSerializer
from .models import Question, Choice, Answer


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            self.serializer_class.Meta.depth = 1
        else:
            self.serializer_class.Meta.depth = 0
        return self.serializer_class


"""class ChoiceListViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            self.serializer_class.Meta.depth = 1
        else:
            self.serializer_class.Meta.depth = 0
        return self.serializer_class"""


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            self.serializer_class.Meta.depth = 1
        else:
            self.serializer_class.Meta.depth = 0
        return self.serializer_class

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

#    def create(self, request, id, choice_id):
#        data = {'choice': choice_id, 'question': id}
#        serializer = QuizSerializer(data=data)
#        if serializer.is_valid():
#            quiz = serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



