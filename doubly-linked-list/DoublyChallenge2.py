# Instructions:
# DLL: Reverse (⚡Interview Question)
# Create a new method called reverse that reverses the order of the nodes in the list,
# i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.
# To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that
# they point in the opposite direction. Once you've done this for all nodes, you'll also need to
# update the head and tail pointers to reflect the new order of the nodes.

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


    def reverse(self):
        temp = self.head
        while temp is not None:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev

        self.head, self.tail = self.tail, self.head



my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.print_list()
print("Reverse")
my_doubly_linked_list.reverse()
my_doubly_linked_list.print_list()