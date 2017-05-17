
def cocktail_sort_up(array):
    "Algorithms cocktail(shaker) sort up O(n^2)"
    left = 0
    right = len(array) -1
    while left <= right:
        for i in range(left,right):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1], array[i]
        right -= 1

        for i in range(right,left,-1):
            if array[i-1] > array[i]:
                array[i],array[i-1] = array[i-1], array[i]
        left += 1

    return None


def cocktail_sort_down(array):
    "Algorithms cocktail(shaker) sort down O(n^2)"
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1

        for i in range(right, left, -1):
            if array[i - 1] < array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1

    return None


def unittest():
    print("running unittest...")
    try:
        # test sort down
        a = [x for x in range(0, 10)]
        cocktail_sort_down(a)
        k = 0
        while k < (len(a) - 1):
            if a[k] < a[k + 1]:
                print("Test failed.Sort down didn't work.")
                break
            k += 1
        # test sort up
        k = 0
        cocktail_sort_up(a)
        while k < (len(a) - 1):
            if a[k] > a[k + 1]:
                print("Test failed.Sort down didn't work.")
                break
            k += 1
    except:
        print('Test failed. Other errors in code')
    print("finish...")


if __name__ == '__main__':
    unittest()