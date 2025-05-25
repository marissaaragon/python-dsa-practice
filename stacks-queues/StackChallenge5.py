# Instructions: Stack: Sort Stack (⚡Interview Question)
# The sort_stack function takes a single argument, a Stack object.
# The function should sort the elements in the stack in ascending order
# (the lowest value will be at the top of the stack) using only one additional stack.
# The function should use the pop, push, peek, and is_empty methods of the Stack object.
# Note: This is a new function, not a method within the Stack class.

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

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

def sort_stack(stack):
    temp_stack = Stack()

    while not stack.is_empty():
        current = stack.pop()

        while not temp_stack.is_empty():
            top = temp_stack.peek()
            if top is not None and top > current:
                stack.push(temp_stack.pop())
            else:
                break

        temp_stack.push(current)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("Stack after sort_stack:")
my_stack.print_stack()





