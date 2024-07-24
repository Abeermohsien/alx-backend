#!/usr/bin/env python3
"""base.
"""


class BaseCaching():
    """basecaching"""
    MAX_ITEMS = 4

    def __init__(self):
        """ startingzes the cache.
        """
        self.cache_data = {}

    def print_cache(self):
        """return cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """creating item in the cache.
        """
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        """return itwm
        """
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)
