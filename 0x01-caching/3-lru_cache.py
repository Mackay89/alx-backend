#!/usr/bin/env python3
"""LRUCache module."""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache class inherits from BaseCaching."""

    def __init__(self):
        """Initialize the LRUCache class."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        # If the item already exists, move it to the end
        # to mark it as recently used
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        # Add or update the item in the cache
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the least recently used item (LRU)
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None:
            return None
        return self.cache_data.get(key, None)
