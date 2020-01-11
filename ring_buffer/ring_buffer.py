from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # current refers to the current item that needs to be removed or replaced
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #Check if the length is less than the capacity. If so it does not need any replacement.
        # It just needs to be added to the double linked list
        # Also if the length is the same as capacity then the first item pushed in will be the
        # one to be replaced.
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            if (self.storage.length == self.capacity):
                self.current = self.storage.head
        else:
            if (self.current is self.storage.head):
                print("------CURRENT IS HEAD ----------")
                self.storage.head.value = item
                self.current = self.storage.head.next
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        i = 1
        current_node = self.storage.head
        while (i < self.storage.length + 1):
            if (current_node.value is not None):
                list_buffer_contents.append(current_node.value)
            current_node = current_node.next
            i += 1

        return list_buffer_contents

ring_buffer = RingBuffer(5)
ring_buffer.append('a')
ring_buffer.append('b')
ring_buffer.append('c')
ring_buffer.append('d')
print(ring_buffer.storage.length)
print(ring_buffer.get())
ring_buffer.append('e')
print(ring_buffer.storage.length)
print(ring_buffer.get())
ring_buffer.append('f')
print(ring_buffer.storage.length)
print(ring_buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
