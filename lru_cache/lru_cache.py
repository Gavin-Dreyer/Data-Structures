from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list.py')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.storage.move_to_end(node)
            return node.value
        else:
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        entry = {key: value}
        [k] = entry.keys()

        # check for key in cache
        if k in self.cache:
            # if in cache, update the current value
            self.storage.add_to_tail(value)
            self.cache[k] = self.storage.tail

        # if cache is full
        if self.size == self.limit:
            # remove LRU node from dll
            temp = ''
            for ke, va in self.cache.items():
                if va.value == self.storage.head.value:
                    temp = ke

            self.storage.remove_from_head()
            # remove LRU item from cache
            del self.cache[temp]
            self.size -= 1

        # adding entry to dll
        self.storage.add_to_tail(value)
        # assigning newest node to cache
        self.cache[k] = self.storage.tail
        # incrementing size of cache
        self.size += 1

        # for j, k in self.cache.items():
        #     print(j, k.value, 'after')

        # if key in self.cache:
        #     node = self.cache[key]
        #     node.value = (key, value)
        #     self.storage.move_to_end(node)
        #     return

        # if self.size == self.limit:
        #     del self.cache[self.storage.head.value[0]]
        #     self.storage.remove_from_head()
        #     self.size -= 1

        # self.storage.add_to_tail((key, value))
        # self.cache[key] = self.storage.tail
        # self.size += 1
