class Node:
    def __init__(self, value, next_node=None):
        # the value that the node is holding 
        self.value = value 
        # reference to the next node in the linked list
        self.next_node = next_node

    # method to get the value of the node 
    def get_value(self):
        return self.value

    # method to get the node's `next_node`
    def get_next(self):
        return self.next_node

    # method to update the node's `next_node` to the input node 
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a Node
        new_node = Node(value)
        # check if the Linked List is empty 
        if self.head is None and self.tail is None:
            # set head and tail to the new node 
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node 
        else:
            # update the last node's `next_node` to the new node 
            self.tail.set_next(new_node)
            # update `self.tail` to point the new node we just added 
            self.tail = new_node

    def remove_tail(self):
        # check if the linked list is empty 
        if self.head is None and self.tail is None:
            return None
        
        # check if the linked list has only one node 
        if self.head == self.tail:
            # store the node we're going to remove's value 
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # otherwise, the linked list has more than one Node 
        else:
            # store the last Node's value in a nother variable so we can return it 
            val = self.tail.get_value()
            # we need to set `self.tail` to the second-to-last Node
            # the only way we can do this, is by traversing the whole linked list
            # from the beginning 
            
            # starting from the head, we'll traverse down to the second-to-last Node 
            # init another reference to keep track of where we are in the linked 
            # list as we're iterating 
            current = self.head

            # keep iterating until the node after `current` is the tail
            while current.get_next() != self.tail:
                # keep iterating 
                current = current.get_next()

            # set `self.tail` to `current`
            self.tail = current
            # set the new tail's `next_node` to None
            self.tail.set_next(None) 
            return val
            
    def remove_head(self):
        # check if the linked list empty 
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node 
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            # store the old head's value that we need to return 
            val = self.head.get_value()
            # set `self.head` to the old head's `next_node`
            self.head = self.head.get_next()
            # return the old_head's value 
            return val

# Should have the methods: push, pop, and len.
# push adds an item to the top of the stack.
# pop removes and returns the element at the top of the stack
# len returns the number of elements in the stack.

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         self.size -= 1
#         return self.storage.pop()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value) 
        self.size += 1
        

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()
        
        

