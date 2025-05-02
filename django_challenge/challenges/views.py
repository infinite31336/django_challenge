from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def monthly_challenge(request, month):
    message = ''
    if month == 'january':
      message = 'Eat no meat for the entire month!'
    elif month == 'february':
      message = 'Walk at least 20 minutes every day!'
    elif month == 'march':
      message = 'Learn Django for at least 20 minutes every day!'
    else:
       return HttpResponseNotFound('This month is not supported!')
    return HttpResponse(message)