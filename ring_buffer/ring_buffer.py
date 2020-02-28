from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if not full add to storage
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        
        else:
            # initial value override
            if self.current is None:
                self.current = self.storage.head

            self.current.value = item

            # setting up the next override to the next node
            if self.current.next:
                self.current = self.current.next
            
            # if there is not a next node set next override to the head
            else:
                self.current = self.storage.head



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        current = self.storage.head

        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
