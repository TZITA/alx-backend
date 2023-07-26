#!/usr/bin/env python3
""" FIFO cache"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache class"""
    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
