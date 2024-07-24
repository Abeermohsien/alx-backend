#!/usr/bin/env python3
"""module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """returning an item to dicationary"""
    def put(self, key, item):
        """creating item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ return an item key
        """
        return self.cache_data.get(key, None)
