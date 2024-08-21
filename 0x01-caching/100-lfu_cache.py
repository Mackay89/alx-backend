#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict

class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the LFUCache class
        """
        super().__init__()
        self.cache_data = {}
        self.freq = defaultdict(int)  # Dictionary to track frequencies
        self.order = OrderedDict()  # Ordered dict to track the LRU order of items

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            # Update existing item
            self.cache_data[key] = item
            self.freq[key] += 1
            # Move the item to the end of the order list
            self.order.move_to_end(key)
        else:
            # Add new item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used items
                min_freq = min(self.freq.values())
                # Collect all keys with the minimum frequency
                lfu_keys = [k for k, v in self.freq.items() if v == min_freq]
                
                # If there are multiple items with the same minimum frequency, use LRU to discard
                if len(lfu_keys) > 1:
                    lru_key = next(iter(self.order))  # Get the least recently used key among LFU keys
                else:
                    lru_key = lfu_keys[0]
                
                # Discard the LFU item
                del self.cache_data[lru_key]
                del self.freq[lru_key]
                del self.order[lru_key]
                print("DISCARD: {}".format(lru_key))
            
            # Add the new item
            self.cache_data[key] = item
            self.freq[key] = 1
            self.order[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Update frequency and move item to end of the order list
        self.freq[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]

