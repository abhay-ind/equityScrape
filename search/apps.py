from django.apps import AppConfig
import redis
from django.conf import settings


class SearchConfig(AppConfig):
    name = "search"
    redis_instance = redis.StrictRedis(
        host=settings.REDIS_HOST, port=settings.REDIS_PORT,password='lh9EzEtpVfsD4Dy9nAFkzeMkaghG09AS', db=0
    )
