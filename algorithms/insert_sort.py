
import time

def insert_sort_up(array):
    "Algorithm insert sort O(n^2)"
    for i in range(0,len(array)):
        x = array[i]
        j = i
        while (j>0) and (array[j-1] > x):
            array[j] = array[j-1]
            j = j-1
        array[j] = x
    return None

def insert_sort_down(array):
    "Algorithm insert sort O(n^2)"
    for i in range(0,len(array)):
        x = array[i]
        j = i
        while (j>0) and (array[j-1] < x):
            array[j] = array[j-1]
            j = j-1
        array[j] = x
    return None

def unittest():
    print("running unittest...")
    try:
        # test sort up
        a = [x for x in range(1000, 0, -1)]
        insert_sort_up(a)
        k = 0
        while k < (len(a) -1) :
            if a[k] > a[k + 1]:
                print("Test failed.Sort up didn't work.")
                break
            k += 1
        # test sort down
        k = 0
        start = time.time()
        insert_sort_down(a)
        end = time.time()
        while k < (len(a) - 1):
            if a[k] < a[k + 1]:
                print("Test failed.Sort down didn't work.")
                break
            k += 1
        print('sorting 1000 elements(worst case):', str(end - start))
    except:
        print('Test failed. Other errors in code')
    print("finish...")

if __name__ == '__main__':
    unittest()