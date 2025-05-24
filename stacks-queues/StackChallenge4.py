# Instructions:
# Stack: Reverse String (⚡Interview Question)
# The reverse_string function takes a single parameter string, which is the string you want to reverse.
# Return a new string with the letters in reverse order.

class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def is_empty(self):
        return len(self.stack_list) == 0

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)


def reverse_string(str):
    stack = Stack()
    rev_str = ""

    for l in str:
        stack.push(l)

    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


my_string = 'hello'
print ( reverse_string(my_string) )
