#!/usr/bin/env python3
"""module for MRU cache"""
from datetime import datetime

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU cache class implementing it's functions"""

    def __init__(self):
        """initializing the MRU Cache"""
        super().__init__()
        self.order = {}

    def put(self, key, item):
        """adds data to the cache"""
        if key is None or item is None:
            return

        if (len(self.cache_data) == self.MAX_ITEMS) and (
                key not in self.cache_data):
            drop_k = self.remove_least_recent()
            print("DISCARD:", drop_k)

        self.order[key] = datetime.now()
        self.cache_data[key] = item

    def get(self, key):
        """gets key value from the cache"""
        if key is None:
            return None
        self.order[key] = datetime.now()
        return self.cache_data.get(key, None)

    def remove_least_recent(self):
        """remove most recent entry from cache data"""
        least_recent = list(self.order.items())[0]

        for key in self.order:
            if self.order[key] > least_recent[1]:
                least_recent = (key, self.order[key])

        if (least_recent[0] in self.order) and (
                least_recent[0] in self.cache_data):
            del self.order[least_recent[0]]
            del self.cache_data[least_recent[0]]
        return least_recent[0]
