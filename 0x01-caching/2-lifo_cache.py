#!/usr/bin/env python3
"""LIFO cache"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class"""
    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last item (LIFO)
                last_key = self.stack.pop()
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
