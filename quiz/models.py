from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    image = models.FileField(upload_to="question_image", unique=False, blank=True, null=True)

    def __str__(self):
        return ('1' + self.question_text)


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    questions = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    choice = models.ForeignKey(Choice, related_name='quizzes', on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)


    """def __str__(self):
        return self.questions"""
