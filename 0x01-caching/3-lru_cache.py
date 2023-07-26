#!/usr/bin/env python3
"""LRU CACHE"""


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRU cache class"""
    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.queue.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None

