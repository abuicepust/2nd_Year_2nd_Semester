# Department of ICE, Pabna University of Science and Technology
# Name: Md. Abu Yousuf
# Roll: 180640
# Session: 2017-2018
# Course Code: ICE-2202
# Course Title: Data Structure and Algorithm Sessional

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
num=int(input("Enter how many number for push in queue : "))
print("Enter the numbers")
for i in range(num):
    q.enqueue(int(input()))
print("Now queue situtation : ")
q.display()
q.dequeue()
q.display()
print("Queue size is ",q.size())
