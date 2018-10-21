from django.db import models

# Create your models here.

class TelegramUser(models.Model):
	telegramId = models.IntegerField()
	intro_question_index = models.IntegerField(default=0)

	def __str__(self):
		return str(self.telegramId)

class IntroQuestion(models.Model):
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text

class Answer(models.Model):
	question = models.ForeignKey(IntroQuestion, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.text

class UserAnswer(models.Model):
	user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user.telegramId) + ": " + self.answer.question.text + " -> " + self.answer.text

class Event(models.Model):
	text = models.CharField(max_length=200)
	body = models.CharField(max_length=4096)
	post_date = models.DateTimeField('the date on which the post will be sent')

	def __str__(self):
		return self.text