
import time

def bubble_sort_up(array):
    "Algorithms bubble sort up O(n^2)"
    change = True
    while change:
        change = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                change = True
    return None


def bubble_sort_down(array):
    "Algorithms bubble sort down O(n^2)"
    change = True
    while change:
        change = False
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change = True
    return None

def unittest():
    print("running unittest...")
    try:
        # test sort down
        a = [x for x in range(1000, 0,-1)]
        bubble_sort_up(a)
        k = 0
        while k < (len(a) - 1):
            if a[k] > a[k + 1]:
                print("Test failed.Sort up didn't work.")
                break
            k += 1
        # test sort up
        k = 0
        start = time.time()
        bubble_sort_down(a)
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