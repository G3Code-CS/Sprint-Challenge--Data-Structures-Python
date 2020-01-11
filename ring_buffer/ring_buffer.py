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

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

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
