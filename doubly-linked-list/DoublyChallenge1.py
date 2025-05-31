# Instructions:
# DLL: Swap First and Last (⚡Interview Question)
# Swap the values of the first and last node
# Method name:
# swap_first_last
# Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.print_list()
print("After swap")
my_doubly_linked_list.swap_first_last()
my_doubly_linked_list.print_list()