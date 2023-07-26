#!/usr/bin/env python3
""" LFU CACHE """


BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFU cache class """
    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = {}
        self.freq_keys = {1: []}
        self.min_frequency = 1

    def _update_frequency(self, key):
        """ Helper method to update the frequency of a key """
        frequency = self.frequency.get(key, 0)
        self.frequency[key] = frequency + 1

        if frequency in self.freq_keys:
            self.freq_keys[frequency].remove(key)
            if len(self.freq_keys[frequency]) == 0:
                del self.freq_keys[frequency]

        if not self.freq_keys.get(self.min_frequency):
            self.min_frequency = 1
            self.min_frequency = min(self.min_frequency, frequency + 1)
        
        self.freq_keys.setdefault(frequency + 1, [])
        self.freq_keys[frequency + 1].append(key)

        if frequency == self.min_frequency and not self.freq_keys[frequency]:
            self.min_frequency += 1

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                while not self.freq_keys[self.min_frequency]:
                    self.min_frequency += 1

                lfu_key = self.freq_keys[self.min_frequency].pop(0)
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self._update_frequency(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self._update_frequency(key)
            return self.cache_data[key]
        return None
