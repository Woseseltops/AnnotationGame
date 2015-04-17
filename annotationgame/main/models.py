from django.db import models

# Create your models here.
class Answer(models.Model):
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text;

class Annotation(models.Model):
    question_nr = models.IntegerField()
    answer = models.ForeignKey(Answer)

    def __str__(self):
        return 'Question '+str(self.question_nr)+' is a '+str(self.answer);

class Streak(models.Model):
    playername = models.CharField(max_length=50)
    length = models.IntegerField();

    def __str__(self):
        return self.playername+': '+str(self.length);
