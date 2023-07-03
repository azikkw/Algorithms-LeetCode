class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]

# obj = MinStack()
# obj.push()
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.get_min()
