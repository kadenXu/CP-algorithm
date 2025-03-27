from src.data_structures import Heap


def test_heap_numeric():
    data = [6, 2, 5, 3, 5, 10, 100, 2, 56, 34]
    heap = Heap(data, ascending=False)
    heapified_data = []
    while heap:
        heapified_data.append(heap.pop())
    assert heapified_data == sorted(data, reverse=True)

def test_heap_obj():
    data = [[6, 2, 5], [4, 6], [10, 100], [2, 56], [34]]
    heap = Heap(data, key=lambda x: len(x))

    data.sort(key=lambda x: len(x))
    assert len(data) == len(heap)
    for x in data:
        # check only length as any ordering is fine so long as they are of the same length
        assert len(x) == len(heap.pop())

def test_heap_push():
    heap = Heap()   
    data = range(10)
    heapified_data = []
    for i in data:
        heap.push(i)
    while heap:
        heapified_data.append(heap.pop())
    assert heapified_data == list(data)
        
    