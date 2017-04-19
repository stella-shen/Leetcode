
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.recent_list = list()
        self.cache = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache.has_key(key):
            self.recent_list.remove(key)
            self.recent_list.insert(0, key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self.cache) < self.capacity or self.cache.has_key(key):
            if self.cache.has_key(key):
                self.recent_list.remove(key)
            self.cache[key] = value
            self.recent_list.insert(0, key)
        else:
            lr_key = self.recent_list[-1]
            self.cache.pop(lr_key)
            self.recent_list.remove(lr_key)
            self.cache[key] = value
            self.recent_list.insert(0, key)

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    print cache.get(1)
    print cache.get(3)
    print cache.get(4)
