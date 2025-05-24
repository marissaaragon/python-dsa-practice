# Instructions:
# LL: Remove Duplicates (⚡Interview Question)
# You are given a singly linked list that contains integer values,
# where some of these values may be duplicated.
#Your task is to implement a method called remove_duplicates() within the LinkedList class
# that removes all duplicate values from the list.
# Your method should not create a new list, but rather modify the existing list in-place,
# preserving the relative order of the nodes.

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
        return True

    def remove_duplicates(self):
         values = set()
         current = self.head
         prev = None
         while current:
             if current.value in values:
                 prev.next = current.next
                 self.length -=1
             else:
                 values.add(current.value)
                 prev = current
             current = current.next


ll = LinkedList(5)
ll.append(6)
ll.append(7)
ll.append(7)
ll.append(8)
ll.append(9)
ll.append(10)
ll.print_list()
ll.remove_duplicates()
print("New List:")
ll.print_list()