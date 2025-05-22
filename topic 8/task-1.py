class Heap:
    def __init__(self, heap_type="min"):
        self.data = []
        self.type = heap_type

    def compare(self, a, b):
        if self.type == "min":
            return a < b
        return a > b

    def insert(self, value):
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    def extract_root(self):
        if not self.data:
            return None
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._heapify_down(0)
        return root

    def peek(self):
        return self.data[0] if self.data else None

    def heapify(self, array):
        self.data = array[:]
        for i in reversed(range(len(self.data) // 2)):
            self._heapify_down(i)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.compare(self.data[index], self.data[parent]):
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.data)
        while index < size:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.compare(self.data[left], self.data[smallest]):
                smallest = left
            if right < size and self.compare(self.data[right], self.data[smallest]):
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

min_heap = Heap("min")
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(2)
print(min_heap.extract_root())  # Output: 2

max_heap = Heap("max")
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(20)
max_heap.insert(2)
print(max_heap.extract_root())  # Output: 20
