from django.shortcuts import render
from django.http import HttpResponse
from models import Answer

# Create your views here.
def stimulus(request):

    return render(request,'stimulus.html',{'answers':[answer.text for answer in Answer.objects.all()]})