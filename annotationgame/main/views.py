from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from models import Answer, Annotation
from annotationgame.settings import STIMULI_FILE_LOCATION
from random import randrange

# Create your views here.
def stimulus(request):

    all_stimuli = open(STIMULI_FILE_LOCATION).readlines();
    random_stimulus_index = randrange(len(all_stimuli));

    return render(request,'stimulus.html',{'answers':Answer.objects.all(),
                                           'stimulus_index':random_stimulus_index,
                                           'stimulus_text':all_stimuli[random_stimulus_index]})

#@require_http_methods(["POST"])
def add_answer(request,stimulus_index,answer_pk):

    answer = Answer.objects.get(pk=answer_pk);
    Annotation(question_nr = stimulus_index,answer=answer).save();

    return HttpResponse(stimulus_index+answer_pk);