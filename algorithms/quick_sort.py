import time

def stooge_sort(a,i,j):
    if a[i] > a[j]:
        a[i],a[j] = a[j],a[i]
    if i+1 >= j: return
    k = int((j-i+1)/3)
    stooge_sort(a,i,j-k)
    stooge_sort(a,i+k,j)
    stooge_sort(a,i,j-k)

def partition(a, p, r):
    x = a[p]
    i = p - 1
    j = r + 1
    while True:
        while True:  # replace for repeat..until
            j -= 1
            if a[j] <= x:
                break
        while True:
            i += 1
            if a[i] >= x:
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            return j

def quick_sort(array,p,r):
    'simple algorithm'
    if p < r:
        q = partition(array,p,r)
        quick_sort(array,p,q)
        quick_sort(array,q+1,r)



def unittest():
    #TODO (in simple quick_sort): recursion error -> max depth
    print("running unittest...")
    try:
        a = [x for x in range(1000, 0, -1)]
        start = time.time()
        stooge_sort(a,0,len(a)-1)
        print(a)
        end = time.time()
        k = 0
        while k < (len(a) - 1):
            if a[k] > a[k + 1]:
                print("Test failed.Sort up didn't work.")
                break
            k += 1
        print('sorting 1000 elements(worst case):', str(end - start))
    except:
        print('Test failed. Other errors in code')
    print("finish...")




if __name__ == '__main__':
    unittest()