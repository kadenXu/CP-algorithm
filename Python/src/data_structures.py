import heapq


class Heap:
    def __init__(self, data=None, *, key=lambda x: x, ascending=True, **kwargs):
        self._comparator = key
        self._ascending = ascending
        self._heap = [(self._construct_key(x), x) for x in data] if data else []
        heapq.heapify(self._heap)

    def _construct_key(self, element):
        return self._comparator(element) * (1 if self._ascending else -1)

    def push(self, element):
        heapq.heappush(self._heap, (self._construct_key(element), element))

    def pop(self):
        data = heapq.heappop(self._heap)
        return data[1]

    def __len__(self):
        return len(self._heap)
