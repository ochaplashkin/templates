import time

def shell(a):
    b = len(a)
    k = int(b / 2)
    while k > 0:
        for i in range(1,b-k,1):
            j = i
            while (j>=1) and (a[j]>a[j+k]):
                a[j],a[j+k] = a[j+k],a[j]
                j -= 1
        k = int(k / 2)
    #bad variant
    #TODO: implemented correct algorithm
    save = a.pop(0)
    a.append(save)

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