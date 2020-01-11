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
    # TO BE COMPLETED
    # The last node becomes the head
    # The links are fully reversed. So loop through and push the .next = .next.next
    # check if there is a head
    if not self.head:
          return self.head
    current_node = self.head
    previous_node = None
    next_node = current_node.next_node
    while (next_node):
        # Because we are reversing the order
        current_node.next_node = previous_node
        previous_node = current_node
        current_node = next_node
        next_node = current_node.next_node
    current_node.next_node = previous_node #For the last node
    self.head = current_node
    return self.head.value

  def __str__(self):
      arr = []
      if (self.head is not None):
        current_node = self.head
        while (current_node.next_node):
            arr.append(current_node.value)
            current_node = current_node.next_node
        arr.append(current_node.value)
      return str(arr)

silly = LinkedList()
silly.add_to_head('a')
silly.add_to_head('b')
silly.add_to_head('c')
silly.reverse_list()
print(silly)