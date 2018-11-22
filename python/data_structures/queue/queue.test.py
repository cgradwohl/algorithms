from queue import Queue

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()
n = q.dequeue()

print q
print n


