# Instructions: Stack: Parentheses Balanced (⚡Interview Question)
# Check to see if a string of parentheses is balanced or not.
# By "balanced," we mean that for every open parenthesis,
# there is a matching closing parenthesis in the correct order.
# For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string.
# On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match,
# so it is not balanced.
# Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.
# Your program should take a string of parentheses as input and return True if it is balanced,
# or False if it is not.
# To solve this problem, use a Stack data structure.
# Function name: is_balanced_parentheses
#Remember: this is not a method within the Stack class, this is a separate function.

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

def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == "(":
            stack.push(p)
        elif p == ")":
            if stack.is_empty() or stack.pop() != "(":
                return False
    return stack.is_empty()

balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'

print( is_balanced_parentheses(balanced_parentheses) )

print( is_balanced_parentheses(unbalanced_parentheses) )



