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
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if self.storage.__len__() > 0:
            (cur_node, val) = self.storage.get_value(key)
            self.storage.move_to_end(cur_node)
            return val
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

        if self.storage.__len__() < self.limit:
            self.storage.add_to_tail(entry)
        else:
            if self.storage.check_dll_to_update(key, value) == True:
                self.storage.check_dll_to_update(key, value)
            else:
                self.storage.remove_from_head()
                self.storage.add_to_tail(entry)
