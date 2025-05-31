# Instructions:
# DLL: Swap Nodes in Pairs (⚡Interview Question)
# You are given a doubly linked list.
# Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list.
# The method should not take any input parameters.
# Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next

            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            second_node.prev = prev
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node

            self.head = first_node.next
            prev = first_node

        self.head = dummy.next
