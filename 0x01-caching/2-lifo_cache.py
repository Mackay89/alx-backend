#!/usr/bin/env python3
"""LIFOCache module

This module implements a LIFO (Last In, First Out) caching mechanism.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class inherits from BaseCaching

    This class implements a LIFO caching system. It uses a dictionary
    to store items and remove the most recently added item when the
    cache exceeds the maximum allowed items.
    """

    def __init__(self):
        """Initialize the LIFOCache class"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache

        Args:
            key (str): The key to identify the item.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        # Add or update the item in the cache
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the last item added (LIFO)
            last_key = next(reversed(self.cache_data))
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """Get an item from the cache

        Args:
            key (str): The key to identify the item.

        Returns:
            The item associated with the key, or None if the key is not
            found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
