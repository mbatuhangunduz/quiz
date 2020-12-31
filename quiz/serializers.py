from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Question, Choice, Answer


class AnswerSerializer(serializers.ModelSerializer):
    #choices = serializers.ReadOnlyField(source='choice.choice_text')
    #question_text = serializers.ReadOnlyField(source='questions.question_text')

    class Meta:
        model = Answer
        fields = ['id', 'questions', 'choice']

        """extra_kwargs = {"questions":
                            {"write_only": True, "required": True},
                        "choice": {"write_only": True, "required": True}
                        }"""


class ChoiceSerializer(serializers.ModelSerializer):
    # answers = AnswerSerializer(many=True, required=False)
    count_answers = serializers.SerializerMethodField()
    #questions = serializers.StringRelatedField()
    class Meta:
        model = Choice
        fields = ['id', 'choice_text',  'count_answers', 'questions']

    def get_count_answers(self, obj):
        return obj.answers.count()


class QuestionSerializer(serializers.ModelSerializer):
    #choices = serializers.StringRelatedField(many=True, )
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = ['id', 'choices', 'question_text', 'image']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice in choices_data:
            Choice.objects.create(questions=question, **choice)
        return question

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get('question_text', instance.question_text)

        choices_data = validated_data.pop('choices')
        if choices_data:
            #instance.choices.clear()
            Choice.objects.bulk_create(
                [
                    Choice(questions=instance, **choice)
                    for choice in choices_data
                ],
            )
        instance.save()
        return instance


class QuestionPartialUpdateSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'choices', 'question_text', 'image']


class QuestionSerializer1(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'choices', 'question_text', 'image']

    def update(self, instance, validated_data):
        choices_data = validated_data.pop('choices')
        choices = instance.choices.all()
        choices = list(choices)
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.save()

        for choice_data in choices_data:
            choice = choices.pop(0)
            choice.choice_text = choice_data.get('choice_text', choice.choice_text)
            choice.save()
        return instance



    """def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["choices"] = ChoiceSerializer(instance.choices.all(), many=True).data
        return rep"""




