from collections import deque

class Queue:
    def __init__(self):
        self.list = deque([])

    def __str__(self):
        return str(self.list)
    
    def __len__(self):
        return len(self.list)

    def dequeue(self):
        node = self.list.popleft()
        return node

    def enqueue(self, node):
        self.list.append(node)