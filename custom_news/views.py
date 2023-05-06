
from django.http import JsonResponse
import requests
from custom_news.models import News
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from custom_news.forms import *
import ast
from .models import Custom_user, News
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def get_news(request):
    url = "https://api.marketaux.com/v1/news/all"
    params = {
        "symbols": "TSLA,AMZN,MSFT",
        "filter_entities": "true",
        "language": "en",
        "api_token": "CgUxphZmoU3SLdRBpT2kLpYQWgCULi9H7YheTwJG"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        return JsonResponse(news_data)
    else:
        return JsonResponse({"error": f"Error: {response.status_code}"})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("User not valid")
    else:
        form = LoginForm()
        return render(request, "custom_news/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def news(request):
    news_items = News.objects.all()
    context = {'news_items': news_items}
    return render(request, 'custom_news/news.html', context)

def custom_news(request):
    if request.user.is_authenticated:
        user = Custom_user.objects.get(pk=request.user.pk)
        interests = ast.literal_eval(user.interest) 

        news_items = News.objects.filter(symbol__in=interests)
    else:
        news_items = News.objects.none()

    context = {'news_items': news_items}
    return render(request, 'custom_news/custom_news.html', context)

def add_interest(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        user = Custom_user.objects.get(pk=request.user.pk)

        # Convert the string representation of interests to a list
        interests = ast.literal_eval(user.interest)

        # Check if the symbol is not already in the interests
        if symbol not in interests:
            interests.append(symbol)
            user.interest = str(interests)  # Convert the list back to a string representation
            user.save()

    return HttpResponseRedirect(reverse('custom_news'))

def remove_interest(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        user = Custom_user.objects.get(pk=request.user.pk)

        # Convert the string representation of the list to an actual list
        interests_list = ast.literal_eval(user.interest)

        if symbol in interests_list:
            interests_list.remove(symbol)
            user.interest = str(interests_list)  # Convert the list back to a string representation
            user.save()

    return HttpResponseRedirect(reverse('custom_news'))