import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "custom_news_feed.settings")
import django
django.setup()

import requests
import json
from custom_news.models import News, Entity, Highlight
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
    
    news_items = news_data['data']

    for news_item_data in news_items:
        news_item = News(
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
            relevance_score=news_item_data["relevance_score"]
        )
        news_item.save()

        for entity_data in news_item_data["entities"]:
            entity = Entity(
                symbol=entity_data["symbol"],
                name=entity_data["name"],
                exchange=entity_data["exchange"],
                exchange_long=entity_data["exchange_long"],
                country=entity_data["country"],
                type=entity_data["type"],
                industry=entity_data["industry"],
                match_score=entity_data["match_score"],
                sentiment_score=entity_data["sentiment_score"],
                news=news_item
            )
            entity.save()

            for highlight_data in entity_data["highlights"]:
                highlight = Highlight(
                    highlight=highlight_data["highlight"],
                    sentiment=highlight_data["sentiment"],
                    highlighted_in=highlight_data["highlighted_in"],
                    entity=entity
                )
                highlight.save()

else:
    print(f"Error: {response.status_code}")