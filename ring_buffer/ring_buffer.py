from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.oldest = None

    def append(self, item):

        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.oldest = (self.storage.tail)

        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)

        elif self.storage.length == self.capacity:

            if self.oldest is not None:
                x = self.oldest.next
                self.oldest.value = item
    
            else:
                x = self.storage.head.next
                self.storage.head.value = item


            self.oldest = x
            
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current is not None:

            list_buffer_contents.append(current.value)
            current = current.next

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
