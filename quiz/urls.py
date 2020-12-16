
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('questions', views.QuestionViewSet)
#router.register('choices', views.ChoiceListViewSet)
router.register('answer', views.AnswerViewSet, basename='quiz')
#router.register(r'answer/(?P<id>[0-9]+)', views.ChoiceViewSet, basename='answers')


urlpatterns = [
    path("", include(router.urls)),
]

