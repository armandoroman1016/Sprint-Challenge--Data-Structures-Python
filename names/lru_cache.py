from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()
        self.limit = limit
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
# TODO SET CACHE TO HOLD A DICTIONARY WITH KEY AS KEYNAME: AND VALUE AS NODE'S KEY VALUE PAIRS
# ? node = (key, value)
# ? inside cache = (node[0], node) 

    def get(self, key):
        
        current = self.storage.head

        not_found = True

        if self.storage.__len__() == 0:
            return None
        
        while current is not None:

            if key == current.value :

                not_found = False

                self.storage.move_to_front(current)

                return self.cache.get(key)
            
            current = current.next
        
        if not_found:

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

        if self.storage.__len__() == 0:
            self.storage.add_to_head(key)
            self.cache[key] = value
        
        elif self.storage.__len__() <= self.limit:

            current = self.storage.head
            found = False

            while current is not None:
                
                if current.value == key:
                    self.storage.move_to_front(current)
                    self.cache[key] = value
                    found = True
                    break
                else:
                    current = current.next
            
            if not found:

                if self.storage.__len__() < self.limit:
                    self.storage.add_to_head(key)
                    self.cache[key] = value

                else:
                    self.cache.pop(self.storage.tail.value)    
                    self.storage.delete(self.storage.tail)
                    self.storage.add_to_head(key)
                    self.cache[key] = value
        
