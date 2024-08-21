#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching
    """
    
    def __init__(self):
        """ Initialize the BasicCache class
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

