# Generated by Django 4.2 on 2023-04-29 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('exchange', models.CharField(max_length=255)),
                ('exchange_long', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('match_score', models.FloatField()),
                ('sentiment_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('keywords', models.TextField(blank=True)),
                ('snippet', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField()),
                ('language', models.CharField(max_length=2)),
                ('published_at', models.DateTimeField()),
                ('source', models.CharField(max_length=255)),
                ('relevance_score', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.TextField()),
                ('sentiment', models.FloatField()),
                ('highlighted_in', models.CharField(max_length=255)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highlights', to='custom_news.entity')),
            ],
        ),
        migrations.AddField(
            model_name='entity',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='custom_news.news'),
        ),
    ]
