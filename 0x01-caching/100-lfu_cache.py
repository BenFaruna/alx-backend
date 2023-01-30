#!/usr/bin/env python3
"""module for LFU cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU cache class implementing it's functions"""

    def __init__(self):
        """initializing the MRU Cache"""
        super().__init__()
        self.cache_count = {}
        self.LFUorder = []

    def put(self, key, item):
        """adds data to the cache"""
        if key is None or item is None:
            return None

        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            discarded = self.LF_remover()
            print("DISCARDED:", discarded)

        self.cache_data[key] = item
        if key in self.cache_count:
            self.cache_count[key] += 1
        else:
            self.cache_count[key] = 1
            self.LFUorder.append(key)


    def get(self, key):
        """gets key value from the cache"""
        if key is None:
            return

        if key in self.cache_data:
            self.cache_count[key] += 1
            self.LFUorder.remove(key)
            self.LFUorder.append(key)
        return self.cache_data.get(key)

    def LF_remover(self):
        """removes the least items in self.cached_data"""
        order = self.LFUorder
        LF = order[0]
        LFcount = self.cache_count[LF]
        for data in order:
            if self.cache_count[data] < LFcount:
                LF = data
                LFcount = self.cache_count[data]

        self.LFUorder.remove(LF)
        self.cache_count.pop(LF)
        self.cache_data.pop(LF)
        return LF
