
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    def enqueue(self, data):  # add value
        if (self.tail + 1) % self.size == self.head:
            print("queue is full")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.head] = data
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("queue is empty")
        elif self.head == self.tail:
            temp = self.queue[self.tail]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head+1) % self.size
            return temp


# queue = CircularQueue(3)
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(30)


x = [None] * 3

print(len(x))
