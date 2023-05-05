from django.db import models

class News(models.Model):
    uuid = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    keywords = models.TextField(blank=True)
    snippet = models.TextField()
    url = models.URLField()
    image_url = models.URLField()
    language = models.CharField(max_length=2)
    published_at = models.DateTimeField()
    source = models.CharField(max_length=255)
    relevance_score = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Entity(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='entities')
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    exchange = models.CharField(max_length=255)
    exchange_long = models.CharField(max_length=255)
    country = models.CharField(max_length=2)
    type = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    match_score = models.FloatField()
    sentiment_score = models.FloatField()
    
    def __str__(self):
        return self.name

class Highlight(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='highlights')
    highlight = models.TextField()
    sentiment = models.FloatField()
    highlighted_in = models.CharField(max_length=255)

    def __str__(self):
        return self.highlight[:50] + '...'