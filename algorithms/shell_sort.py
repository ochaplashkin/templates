import time

def shell(a):
    "Algorithm shell sort "
    if len(a) <= 4000:
        d = 701 #with this value time complexity = O(N(logN)^2)
    else:
        d = int(len(a) / 2)
    while d > 0:
        k = True
        while k:
            k = False
            for i in range(0,len(a)-d,1):
                if a[i] > a[i+d]:
                    a[i],a[i+d] = a[i+d],a[i]
                    k = True
        d = int(d / 2)

def unittest():
    print("running unittest...")
    try:
        a = [x for x in range(1000, 0, -1)]
        start = time.time()
        shell(a)
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