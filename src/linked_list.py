# LINKED LIST - a chain of nodes. Each node holds one value and points to the next node.
# Used by:
#   history.py - Navigation History (a Stack built on top of this list)
#   stats.py   - Group buildings by category (one list per category)
#
# Unlike a plain Python list, nothing is stored side by side in memory:
# the only way to reach a node is to start at the head and follow the links.


class Node:
    def __init__(self, data):
        self.data = data    # the value stored in this node
        self.next = None    # the node after this one (None = end of the chain)


class LinkedList:
    def __init__(self):
        self.head = None    # first node
        self.tail = None    # last node (so append does not have to walk the chain)
        self.size = 0

    def is_empty(self):
        return self.head is None

    def push_front(self, data):
        # Add a new node at the head. Used by the Stack (push).
        node = Node(data)
        node.next = self.head
        self.head = node
        if self.tail is None:      # the list was empty, so this node is also the tail
            self.tail = node
        self.size += 1

    def pop_front(self):
        # Remove the head node and return its value. Used by the Stack (pop).
        # Returns None if the list is empty.
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        if self.head is None:      # the list is now empty
            self.tail = None
        self.size -= 1
        return node.data

    def append(self, data):
        # Add a new node at the end (tail).
        node = Node(data)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1