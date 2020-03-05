class Stack:
    class StackNode:
        def __init__(self, data=0, next_node=None ):
            self.nextNode = next_node
            self.data = data

    def __init__(self):
        self.top = None

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty cannot access top!")
        return self.top.data

    def pop(self):
        if self.is_empty():
            raise Exception('Trying to pop from empty stack!')

        removed_data = self.peek()
        self.top = self.top.next_node
        return removed_data

    def push(self, node):
        node.next_node = self.top
        self.top = node

    def is_empty(self):
        return self.top is None

