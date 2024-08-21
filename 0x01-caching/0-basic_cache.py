#!/usr/bin/env python3
"""
Basic caching module.

This module implements a basic caching system using a dictionary for
storing and retrieving items. It extends the BaseCaching class to provide
put and get methods for interacting with the cache.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Represents an object that allows storing and retrieving items from a cache.

    This class inherits from BaseCaching and provides methods for adding
    items to the cache and retrieving them by key. It uses a dictionary
    to store the cache data.
    """

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key (str): The key under which the item will be stored.
            item (any): The item to be stored in the cache.

        If either key or item is None, the method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key (str): The key of the item to be retrieved.

        Returns:
            The item associated with the key, or None if the key is not
            found in the cache.
        """
        return self.cache_data.get(key, None)
