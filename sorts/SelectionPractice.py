# Instructions:
# Selection Sort of LL (⚡Interview Question)
# Assignment:
# Write a selection_sort() method in the LinkedList class that will sort the elements of a linked list
# in ascending order using the selection sort algorithm. The method should update the head and
# tail pointers of the linked list to reflect the new order of the nodes in the list.
# You can assume that the input linked list will contain only integers. You should not use any
# additional data structures to sort the linked list.


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

    def selection_sort(self):
        if self.length < 2:
            return

        current = self.head
        while current.next is not None:
            smallest = current
            inner_current = current.next

            while inner_current is not None:
                if inner_current.value < smallest.value:
                    smallest = inner_current
                inner_current = inner_current.next

            if smallest != current:
                current.value, smallest.value = smallest.value, current.value

            current = current.next

        self.tail = current



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()