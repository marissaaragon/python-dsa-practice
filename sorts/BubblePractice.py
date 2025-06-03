# Instructions:
# Bubble Sort of LL (⚡Interview Question)
# Assignment:
# Write a bubble_sort() method in the LinkedList class that will sort the elements of a
# linked list in ascending order using the bubble sort algorithm. The method should update the head and
# tail pointers of the linked list to reflect the new order of the nodes in the list.
# You can assume that the input-linked list will contain only integers.
# You should not use any additional data structures to sort the linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        if self.length < 2:
            return

        sorted_until = None

        while sorted_until != self.head.next:
            current = self.head
            while current.next != sorted_until:
                next_node = current.next
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                current = current.next
            sorted_until = current

        self.tail = current



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()
