import time

def merge_sort(array):
    "Recursive algorithm sorting in O(N*logN)"
    if len(array) == 1:
        return array
    middle = int(len(array)/ 2)
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left,right)

def merge(left,right):
    "function merge "
    result = []
    while (len(left) > 0) and (len(right)>0):
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

def unittest():
    print("running unittest...")
    try:
        a = [x for x in range(1000, 0, -1)]
        start = time.time()
        new_a = merge_sort(a)
        end = time.time()
        k = 0
        while k < (len(a) - 1):
            if new_a[k] > new_a[k + 1]:
                print("Test failed.Sort up didn't work.")
                break
            k += 1
        print('sorting 1000 elements(worst case):', str(end - start))
    except:
        print('Test failed. Other errors in code')
    print("finish...")

if __name__ == '__main__':
    unittest()