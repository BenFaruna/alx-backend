#!/usr/bin/env python3
"""module for implementing basic cache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """basic cache inheriting from BasciCaching"""

    def put(self, key, item):
        """adds data to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets key value from the cache"""
        if key is None:
            return None

        return self.cache_data.get(key, None)
