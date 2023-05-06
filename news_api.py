import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "custom_news_feed.settings")
import django
django.setup()
from keras.models import load_model
from model_funct import prediction
import requests
from custom_news.models import News
import numpy as np
url = "https://api.marketaux.com/v1/news/all"
params = {
    "symbols": "DDOG,TSLA,AMD,AMZN",
    "filter_entities": "true",
    "language": "en",
    "api_token": "CgUxphZmoU3SLdRBpT2kLpYQWgCULi9H7YheTwJG"
}

model = load_model('senti_model_main.h5')
response = requests.get(url, params=params)

if response.status_code == 200:
    news_data = response.json()

    news_items = news_data['data']

    for news_item_data in news_items:
        news_article = News(
            uuid=news_item_data["uuid"],
            title=news_item_data["title"],
            description=news_item_data["description"],
            keywords=news_item_data["keywords"],
            snippet=news_item_data["snippet"],
            url=news_item_data["url"],
            image_url=news_item_data["image_url"],
            language=news_item_data["language"],
            published_at=news_item_data["published_at"],
            source=news_item_data["source"],
            relevance_score=np.argmax(prediction(news_item_data["title"]))
        )

        entity_data = news_item_data["entities"][0]  
        news_article.symbol = entity_data["symbol"]
        news_article.name = entity_data["name"]
        news_article.exchange = entity_data["exchange"]
        news_article.exchange_long = entity_data["exchange_long"]
        news_article.country = entity_data["country"]
        news_article.type = entity_data["type"]
        news_article.industry = entity_data["industry"]
        news_article.match_score = entity_data["match_score"]
        news_article.sentiment_score = entity_data["sentiment_score"]

        news_article.save()

else:
    print(f"Error: {response.status_code}")