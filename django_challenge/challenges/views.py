from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
   'january': 'Eat no meat for the entire month!',
   'february': 'Walk at least 20 minutes every day!',
   'march': 'Learn Django for at least 20 minutes every day!',
   'april': 'Eat no meat for the entire month!',
   'may': 'Walk at least 20 minutes every day!',
   'june': 'Learn Django for at least 20 minutes every day!',
   'july': 'Eat no meat for the entire month!',
   'august': 'Walk at least 20 minutes every day!',
   'september': 'Learn Django for at least 20 minutes every day!',
   'ocober': 'Eat no meat for the entire month!',
   'november': 'Walk at least 20 minutes every day!',
   'december': 'Learn Django for at least 20 minutes every day!',
}

def index(request):
  list_items = ''
  months = list(monthly_challenges.keys())

  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse('month-challenge', args=[month])
    list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

  response_data = f'<ul>{list_items}</ul>'
  print(response_data)
  return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(month):
       return HttpResponseNotFound('Invalid month')
    
    rederict_month = months[month - 1]
    rederict_path = reverse('month-challenge', args=[rederict_month])
    return HttpResponseRedirect(rederict_path)

def monthly_challenge(request, month):
  try:
    message = monthly_challenges[month]
    response_data = render_to_string('challenges/challenge.html')
    print('monthly_challenge')
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound('<h1>This month is not supported!<h1>')
  