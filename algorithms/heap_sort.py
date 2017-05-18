import time

#TODO: implement correct algorithm build  heap
# ['stop',5,3,17,10,84,19,6,22,9] index [ 0,..]
# begin form array[1] to end array

class Binary_Heap():
    def __init__(self):
        pass

    def parent(self,i):
        return int(i/2)
    def left(self,i):
        return 2*i
    def right(self,i):
        return 2*i+1

    def heapify(self,array,i):
        size = len(array)-1
        l = self.left(i)
        r= self.right(i)
        if (l <= size) and (array[l] > array[i]):
            largest = l
        else:
            largest = i
        if (r <= size) and (array[r] > array[largest]):
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest],array[i]
            self.heapify(array,largest)

    def build_heap(self,array):
        size = len(array)-1
        for i in range(int(len(array)/2),1,-1):
            self.heapify(array,i)
        pass
    def heap_sort(self,array):
        self.build_heap(array)
        for i in range(len(array),2,-1):
            array[1],array[i] = array[i], array[1]
        pass
    def extract_max(self):
        pass
    def insert(self):
        pass

def unittest():
    print('unittest...')
    heap = Binary_Heap()
    a = ['stop',5,3,17,10,84,19,6,22,9]
    print('Array',a)
    heap.build_heap(a)
    print(a)

if __name__ == '__main__':
    unittest()