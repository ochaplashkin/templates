import time

def gnome_sort_up(array):
    "Algorithm gnome sort O(n^2)"
    i = 1
    while i < len(array):
        if not i or array[i - 1] <= array[i]:
            i+=1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i-=1
    return None

def gnome_sort_down(array):
    i = 1
    while i < len(array):
        if not i or array[i - 1] >= array[i]:
            i+=1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i-=1
    return None

def unittest():
    print("running unittest...")
    try:
        # test sort up
        a = [x for x in range(1000, 0, -1)]
        gnome_sort_up(a)
        k = 0
        while k < (len(a) - 1):
            if a[k] > a[k + 1]:
                print("Test failed.Sort up didn't work.")
                break
            k += 1
        # test sort down
        k = 0
        start = time.time()
        gnome_sort_down(a)
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
