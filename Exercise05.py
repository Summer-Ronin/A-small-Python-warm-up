"""
    Building a custom Queue
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[len(self.items) - 1]


if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(9)
    print(q.dequeue())
    print(q.front())
