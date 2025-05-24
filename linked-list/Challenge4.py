# Instructions:
# LL: Find Kth Node From End (⚡Interview Question)
# Method name: find_kth_from_end
# Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.

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

    def find_kth_from_end(self, k):
        slow = self.head
        fast = self.head

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow

# Fast pointer will first check if k is less than the length of the list, otherwise return false
# Fast pointer will be k ahead of slow pointer
# Both pointers will increase until the fast pointer reaches the end
# When fast reaches the end slow pointer will be k away from the end
# Return slow pointer
# O(N)

ll = LinkedList(5)
ll.append(6)
ll.append(7)
ll.append(8)
ll.append(9)
ll.append(10)
print(ll.find_kth_from_end(3))
