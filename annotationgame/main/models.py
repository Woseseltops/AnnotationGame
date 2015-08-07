from django.db import models
from annotationgame.settings import HIGHSCORE_SIZE, MINIMUM_STREAK_FOR_HIGHSCORE

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

def get_highscore():

    streaks = Streak.objects.all()
    return sorted(streaks,key=lambda x: x.length,reverse=True)[:HIGHSCORE_SIZE]

def calculate_minimum_streak_to_enter_highscore():

    highscore = get_highscore()

    if len(highscore) < HIGHSCORE_SIZE:

        #Equal to the score of the last one
        return MINIMUM_STREAK_FOR_HIGHSCORE

    else:

        #Higher than the last one
        return highscore[-1].length + 1