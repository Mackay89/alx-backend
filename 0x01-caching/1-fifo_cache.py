#!/usr/bin/env python3
"""FIFO caching module.

This module implements a FIFO caching mechanism using the OrderedDict
to maintain the order of item insertion.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFO cache class inherits from BaseCaching.

    This class implements a FIFO caching system. It uses an OrderedDict
    to maintain the order of item insertion and remove the oldest item
    when the cache exceeds the maximum allowed items.
    """

    def __init__(self):
        """Initialize the FIFOCache class."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key (str): The key to identify the item.
            item (any): The item to store in the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            # Update the item if it already exists
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the first item added (FIFO)
            oldest_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key (str): The key to identify the item.

        Returns:
            The item associated with the key, or None if the key is not
            found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
