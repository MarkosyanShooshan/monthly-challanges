from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse



monthly_challenges = {
    "january":"Eat no meatfor the entire month!",
    "february": "Walk for at least 20minutes every day!",
    "march":"Learn Django for at least 20minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "julay": "Eat no meat for the entire month!",
    "august":"Walk for at least 20 minutes every day!",
    "september": "Learn a new word in a foreign language every day!",
    "october" :"Sleep for at least 7-8 hours every night!",
    "november":"Practice mindfulness or meditation for 5 minutes every day!",
    "december":"Reflect on your achievements and plan your next year!"
}
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months":months})


     
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args = [redirect_month])
    return HttpResponseRedirect(redirect_path)



def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return render(request,"challenges/challenge.html", {
            "text":challenge_text,
            "month_name":month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!<h1>")