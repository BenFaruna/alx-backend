#!/usr/bin/env python3
"""module for MRU cache"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU cache class implementing it's functions"""

    def __init__(self):
        """initializing the MRU Cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """adds data to the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key in self.cache_data:
                del self.cache_data[key]
                self.order.remove(key)
            else:
                del self.cache_data[self.order[self.MAX_ITEMS - 1]]
                discarded = self.order.pop(self.MAX_ITEMS - 1)
                print("DISCARD:", discarded)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """gets key value from the cache"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
