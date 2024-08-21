#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the LIFOCache class
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache
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
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

