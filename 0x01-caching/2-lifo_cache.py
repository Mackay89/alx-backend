#!/usr/bin/env python3
"""LIFO Caching system."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an LIFO caching system."""

    def __init__(self):
        """Initialize LIFO cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # Existing key, update value
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Cache full, remove last item
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)
