# Redis

## Setup Reddis with Dajango
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://localhost:6379/1",  # Adjust according to your Redis setup
    }
}


## Function to Load Users into Cache
import redis
import json
from django.contrib.auth import get_user_model
from django.conf import settings 

""" 
#Connect to Redis
redis_client = redis.StrictRedis.from_url(settings.CACHES["default"]["LOCATION"], decode_responses=True)

def load_users_into_cache():
    """
    Load all users from DB into Redis on app startup.
    """
    User = get_user_model()
    users = list(User.objects.values("id", "username", "email"))  # Fetch user data
    redis_client.set("cached_users", json.dumps(users))  # Store in Redis
    print("✅ Users loaded into cache") 
"""