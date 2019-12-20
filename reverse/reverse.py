class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    
    current = self.head
    # next and prev variables to keep track of current location
    next = None
    prev = None
    if current.get_next() is None:
        return
    else:
        while current is not None:
    
            next = current.get_next()
    
            # reversing the nodes pointer from pointing forward to point to the previous element
            current.set_next(prev)
    
            # once pointers have been flipped update our 'prev' variable with 'current' node for next iteration
            prev = current
            
            # updating the 'current' variable with the 'next' node for next iteration
            current = next
    
        # updating the head of the linked list
        self.head = prev
    
        # returning linked list
        return self

linked_list = LinkedList()

linked_list.add_to_head(5)
linked_list.add_to_head(10)
linked_list.add_to_head(15)
linked_list.add_to_head(20)

print('b4 head', linked_list.head.next_node.value)
reversed = linked_list.reverse_list()
print(reversed.head.next_node.value)
print('after head', linked_list.head.value)