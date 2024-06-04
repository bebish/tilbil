from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError

from language.models import Language,Level

class Question(models.Model):
    question_text = models.TextField()
    correct_answer = models.TextField()
    var1 = models.TextField()
    var2 = models.TextField()
    var3 = models.TextField()

    def __str__(self) -> str:
        return self.question_text
    
class FillInTheBlankQuestion(models.Model):
    question_text = models.TextField()
    correct_answer = models.TextField()  # правильные слова через пробел
    blank_words = models.TextField()  # слова для выбора через запятую

    def __str__(self) -> str:
        return self.question_text

class TranslateQuestion(models.Model):
    question_text = models.TextField()
    correct_answer = models.TextField()
    user_answer = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.question_text
    

class ListenQuestion(models.Model):
    question_text = models.TextField()
    correct_answer = models.TextField()  # правильные слова через пробел
    blank_words = models.TextField()  # слова для выбора через запятую

    def __str__(self) -> str:
        res = f'listen+ {self.question_text}'
        return res

# class SpeakQuestion(models.Model):
#     question_text = models.TextField()

#     def __str__(self) -> str:
#         res = f'speak+ {self.question_text}'
#         return res

class LessonCategory(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    lesson_level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='categories',blank=True)

    def __str__(self) -> str:
        return self.title



class Lesson(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='lessons')
    level = models.ForeignKey(Level,on_delete=models.CASCADE,related_name='lessons',default=1)
    category = models.ForeignKey(LessonCategory, on_delete=models.CASCADE, related_name='lessons',default=1)
    name = models.CharField(max_length=60)
    tests = models.ManyToManyField(Question, related_name='lessons', blank=True)
    fill_in_the_blank_tests = models.ManyToManyField(FillInTheBlankQuestion, related_name='lessons', blank = True)
    translate_tests = models.ManyToManyField(TranslateQuestion,related_name='lessons',blank=True)
    listen_tests = models.ManyToManyField(ListenQuestion,related_name='lessons',blank=True)
    image = models.ImageField(upload_to='lessons',default='default_lesson.avif')

    def __str__(self) -> str:
        return self.name
    
    @property
    def get_image(self):
        return self.image.url
    
    def check_answers(self, user_answers):
        """
        Проверяет ответы пользователя.

        :param user_answers: Словарь, где ключи - ID вопросов, значения - ответы пользователя.
        :return: Список с результатами проверки (True, если ответ правильный, иначе False).
        """
        results = []
        for question in self.tests.all():
            correct_answer = question.correct_answer
            user_answer = user_answers.get(str(question.id), "")
            results.append(correct_answer == user_answer)
        return results
    


class LessonAdmin(admin.ModelAdmin):
    filter_horizontal = ('tests','fill_in_the_blank_tests','translate_tests','listen_tests',) 
