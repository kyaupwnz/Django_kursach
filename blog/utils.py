from django.conf import settings
from django.core.cache import cache

from blog.models import Record


def cache_blog(self):
    queryset = Record.objects.all()
    if settings.CACHE_ENABLED:
        key = 'blog'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)
        return cache_data
    return queryset
