import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        heapq.heappush(self.heap, (priority, value))

    def dequeue(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.heap)[1]

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0
pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

print(pq.dequeue())  # Output: Task B (priority 1)
print(pq.peek())     # Output: Task C (priority 2)
print(pq.dequeue())  # Output: Task C
print(pq.dequeue())  # Output: Task A
print(pq.dequeue())  # Output: None (empty queue)
