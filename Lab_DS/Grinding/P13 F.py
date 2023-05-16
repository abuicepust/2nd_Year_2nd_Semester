class Queue:
    def __init__(self):
        self.queue = []

    # add an element
    def enqueue(self, item):
        self.queue.append(item)

    # remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # display the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()

num = int(input("Enter how many elements: "))
print("Enter the numbers: ")
for i in range(num):
    q.enqueue(int(input()))
print("Now queue situation: ")
q.display()
q.dequeue()
q.display()
print("Size of the queue: ", q.size())
