from django.apps import AppConfig
import redis
from django.conf import settings
from redislite import Redis



class SearchConfig(AppConfig):
    name = "search"
    redis_instance = Redis('/tmp/redis.db')
    # redis_instance = redis.StrictRedis(
    #     host=settings.REDIS_HOST, port=settings.REDIS_PORT,password='lh9EzEtpVfsD4Dy9nAFkzeMkaghG09AS', db=0
    # )
