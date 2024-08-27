class MyQueue(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        stack = []
        if self.queue:
            while self.queue:
                stack.append(self.queue.pop())
            a = stack.pop()
            while stack:
                self.queue.append(stack.pop())
            if a:
                return a
        
    def peek(self):
        stack = []
        if self.queue:
            while self.queue:
                stack.append(self.queue.pop())
            a = stack.pop()
            self.queue.append(a)
            while stack:
                self.queue.append(stack.pop())
            return a

    def empty(self):
        if self.queue:
            return False
        else:
            return True