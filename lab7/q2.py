class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)

    def peek(self):
        return self.queue[0]


queue = Queue()
print(queue.enqueue(5))
print(queue.enqueue(6))
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
