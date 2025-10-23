class Stack:

    def __init__(self):
        self.line = []

    def is_empty(self):
        return len(self.line) == 0

    def size(self):
        return len(self.line)

    def pop(self):
        if self.line:
            first_item = self.line.pop()
            return first_item
        else:
            print('Stack is empty')

    def peek(self):
        if self.line:
            first_item = self.line[0]
            return first_item
        else:
            print('Stack is empty')

    def push(self, item):
        self.line.append(item)



    