#!/usr/bin/env python3
"""module for LIFO cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache class implementing it's functions"""

    def __init__(self):
        """initializing the LIFO Cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """adds data to the cache"""
        if key is None or item is None:
            return

        if (len(self.cache_data) == self.MAX_ITEMS) and (
                key not in self.cache_data):
            drop_k = self.order.pop()
            del self.cache_data[drop_k]
            print("DISCARD:", drop_k)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """gets key value from the cache"""
        if key is None:
            return None

        return self.cache_data.get(key, None)
