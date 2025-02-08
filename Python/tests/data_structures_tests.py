from src.data_structures import Heap


def heap_test():
    data = [[6, 2, 5], [4, 6], [10, 100], [2, 56], [34]]
    data2 = [6, 2, 5, 3, 5, 10, 100, 2, 56, 34]
    # heap = Heap(data, ascending=False, key=lambda x: len(x))
    heap = Heap(data2, ascending=False)
    while heap:
        print(heap.pop())

