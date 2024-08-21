#!/usr/bin/env python3
"""
FIFO caching module.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and retrieving items
    from a FIFO cache.
    """

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return
        if len(self.queue) >= self.MAX_ITEMS:
            oldest = self.queue.pop(0)
            del self.cache_data[oldest]
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)
