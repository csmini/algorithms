# The stack data structure is very popular in solving many CS problems.
# It's especially used in in problems where you need to track values of older states,
# But more on that in future videos.
# Let's begin by creating a stack in Python.

class Stack:

    def __init__(self):
        self.stack = []
    
    def __repr__(self):
        return f"<Stack {self.stack}>"

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return
