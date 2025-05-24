# Instructions: LL: Partition List (⚡Interview Question)
# You are given a singly linked list implementation in Python that does not have a tail pointer
# (which will make this method simpler to implement).
# You are tasked with implementing a method partition_list(self, x)
# that will take an integer x and partition the linked list such that all nodes with values
# less than x come before nodes with values greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# You need to implement this method as a method of the LinkedList class.
# The method should take an integer x as input. If the linked list is empty, the method should return None.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def partition_list(self, x):
        dummy_less = Node(0)
        dummy_more = Node(0)

        less = dummy_less
        more = dummy_more
        current = self.head

        while current:
            if current.value < x:
                less.next = current
                less = less.next
            else:
                more.next = current
                more = more.next
            current = current.next

        more.next = None
        less.next = dummy_more.next
        self.head = dummy_less.next

        # Create two dummy nodes to store link of the less and greater values
        # Create pointers for less and more
        # While current val is not none
        # If current is less than given x value, set less.next to current val, update less pointer
        # If current is more than x value, set more.next to current val, update more pointer
        # Since more list should be at the end set next to none to end chain
        # Set next value in less to the more list
        # Update head to the beginning of the less list


