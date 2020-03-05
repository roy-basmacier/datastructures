class Queue:
    class QueueNode:
        def __init__(self, data=0, next_node=None):
            self.data = data
            self.next_node = next_node

    def __init__(self):
        self.front = None
        self.end = None

    def add(self, node):
        if self.is_empty():
            self.front = node
            self.end = node
        else:
            self.end.next_node = node
            self.end = node

    def remove(self):
        if self.is_empty():
            raise Exception('Trying to remove from empty queue!')
        data = self.peek()
        self.front = self.front.next_node
        if not self.front:
            self.end = None

        return data

    def peek(self):
        if self.is_empty():
            raise Exception('Trying to peek empty queue!')
        return self.front.data

    def is_empty(self):
        return self.front is None


