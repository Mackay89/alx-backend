#!/usr/bin/env python3
"""MRUCache module."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class inherits from BaseCaching."""

    def __init__(self):
        """Initialize the MRUCache class."""
        super().__init__()
        self.cache_data = {}
        self.order = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        # Add or update the item in the cache
        if key in self.cache_data:
            self.cache_data[key] = item
            # Move the item to the end of the order list to mark it as
            # recently used
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get an item from the cache."""
        if key is None or key not in self.cache_data:
            return None

        # Move the item to the end of the order list to mark it as recently
        # used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
