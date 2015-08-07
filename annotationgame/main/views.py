from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from models import Answer, Annotation, Streak, calculate_minimum_streak_to_enter_highscore, get_highscore
from annotationgame.settings import STIMULI_FILE_LOCATION
from random import randrange

import json

# Create your views here.
def stimulus(request):

    all_stimuli = [line.split('\t')[0] for line in open(STIMULI_FILE_LOCATION)]
    random_stimulus_index = randrange(len(all_stimuli))

    print('Received',request.POST)

    try:
        current_streak = Streak.objects.filter(pk=request.POST['streak_id'])[0]
        current_streak.playername = request.POST['playername']
        current_streak.save()
    except KeyError:
        pass

    return render(request,'stimulus.html',{'answers':Answer.objects.all(),
                                           'stimulus_index':random_stimulus_index,
                                           'stimulus_text':all_stimuli[random_stimulus_index]})

@require_http_methods(["POST"])
def add_answer(request,stimulus_index,answer_pk):

    response = {}

    #Add the answer to the database
    answer = Answer.objects.get(pk=answer_pk);
    Annotation(question_nr=stimulus_index,answer=answer).save()

    #Check and return whether the answer is also correct
    correct_pk = open(STIMULI_FILE_LOCATION).readlines()[int(stimulus_index)].strip().split('\t')[1]
    response['correct'] = correct_pk == answer_pk

    print('Received',request.POST)

    if response['correct']:
        minimum_streak_to_enter_highscore = calculate_minimum_streak_to_enter_highscore()

        #First, see whether this is info to add to an existing streak
        if request.POST['streak_id'] not in [None,'undefined','null']:

            current_streak = Streak.objects.filter(pk=request.POST['streak_id'])[0]
            current_streak.length = request.POST['streak_length']
            current_streak.save()
            response['streak_id'] = current_streak.pk

        #if not, check whether you made the highscore
        elif int(request.POST['streak_length']) >= minimum_streak_to_enter_highscore:

            #If so, add the streak to the database
            new_streak = Streak(playername='Anonymous', length=int(request.POST['streak_length']))
            new_streak.save()
            response['streak_id'] = new_streak.pk
            response['ask_for_name'] = True

        #else, do nothing specail
        else:
            response['streak_id'] = False

    return HttpResponse(json.dumps(response))

def playername(request,streak_id):

    return render(request,'playername.html',{'streak_id':streak_id})

def highscore(request):

    return render(request,'highscore.html',{'highscore':get_highscore()})