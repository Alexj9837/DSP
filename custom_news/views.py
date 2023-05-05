from django.shortcuts import render
from django.http import JsonResponse
import requests
from custom_news.models import News  # Replace 'your_app' with the actual name of your app

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


def news(request):
    news_items = News.objects.all()
    context = {'news_items': news_items}
    return render(request, 'custom_news/news.html', context)