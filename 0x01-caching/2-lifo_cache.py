#!/usr/bin/env python3
"""LIFO Caching module.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching system.
    """

    def __init__(self):
        """Initialize the LIFOCache object.
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the last item put in cache
            discarded_key = next(reversed(self.cache_data))
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key.
        """
        return self.cache_data.get(key, None)
