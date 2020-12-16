from rest_framework import serializers
from .models import Question, Choice, Answer


class ChoiceSerializer(serializers.ModelSerializer):
    #questions = serializers.StringRelatedField(many=True, )
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']


class QuestionSerializer(serializers.ModelSerializer):
    #choices = serializers.StringRelatedField(many=True, )
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'choices', 'image']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(questions=question, **choice_data)
        return question


    """def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["choices"] = ChoiceSerializer(instance.choices.all(), many=True).data
        return rep"""


class AnswerSerializer(serializers.ModelSerializer):
    #choices = serializers.ReadOnlyField(source='choice.choice_text')
    #question_text = serializers.ReadOnlyField(source='questions.question_text')

    class Meta:
        model = Answer
        fields = ['questions', 'choice']

        """def create(self):
            choices = Choice.objects.create(questions=self.kwargs['id'])
            return choices"""

        """extra_kwargs = {"questions":
                            {"write_only": True, "required": True},
                        "choice": {"write_only": True, "required": True}
                        }"""

