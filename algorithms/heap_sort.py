import time

class Binary_Heap():
    def __init__(self):
        self.size = None
        pass

    def parent(self,i):
        return int(i/2)
    def left(self,i):
        return 2*i
    def right(self,i):
        return 2*i+1

    def heapify(self,array,i):
        self.size = len(array)-1
        l = self.left(i)
        r= self.right(i)
        if (l <= self.size) and (array[l] > array[i]):
            largest = l
        else:
            largest = i
        if (r <= self.size) and (array[r] > array[largest]):
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest],array[i]
            self.heapify(array,largest)

    def build_heap(self,array):
        self.size = len(array)-1
        for i in range(int(len(array)/2),1,-1):
            self.heapify(array,i)
        pass
    def heap_sort(self,array):
        #first variant with class heap
        #it's dont'work...
        self.build_heap(array)
        size = len(array)-1
        for i in range(len(array)-1,2,-1):
            array[1],array[i] = array[i], array[1]
            self.size -= 1
            self.heapify(array,1)
        pass
    def extract_max(self):
        pass
    def insert(self):
        pass

def sort(array):
    #second variant without heap class
    #it's don't work...
    #TODO: implement correct variant
    length = len(array) - 1
    leastParent = int(length / 2)
    print(length,leastParent)
    for i in range(leastParent,0,-1):
        moveDown(array,i,length)

    for i in range(length,0,-1):
        if array[0] > array[i]:
            array[0],array[i] = array[i],array[0]
            moveDown(array,0,i-1)

def moveDown(array,first,last):
    largest = 2*first + 1
    while largest <= last:
        if (largest < last) and (array[largest] < array[largest + 1]):
            largest +=1
        if array[largest] > array[first]:
            largest,first = first,largest
            first = largest
            largest = 2*first + 1
        else:
            return [0]

def unittest():
    print('unittest...')
    heap = Binary_Heap()
    a = [8,5,3,1,9,6,0,7,4,2,5]
    print('Array',a,len(a))
    sort(a)
    print('Result',a)



if __name__ == '__main__':
    unittest()