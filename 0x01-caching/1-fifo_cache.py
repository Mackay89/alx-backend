#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict

class FIFOCache(BaseCaching):
    """ FIFOCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the FIFOCache class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache
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
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

