from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
   'december': None,
}

def index(request):
  months = list(monthly_challenges.keys())

  return render(request, 'challenges/index.html', {
     'months': months
  })

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
    return render(request, 'challenges/challenge.html', {
      'month_name': month.capitalize(),
      'text': message
    })
  except:
    response_data = render_to_string('404.html')
    raise Http404()
  