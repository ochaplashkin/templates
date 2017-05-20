import time

#TODO:write comment in algorithm

def heapsort(s):
    #it's correct algorithm
    sl = len(s)
    def swap(pi,ci):
        if s[pi] < s[ci]:
            s[pi], s[ci] = s[ci], s[pi]
    def sift(pi,unsorted):
        i_qt = lambda a,b: a if s[a]>s[b] else b
        while pi*2 + 2 < unsorted:
            qtci = i_qt(pi*2+1,pi*2+2)
            swap(pi,qtci)
            pi = qtci
    for i in  range(int((sl/2))-1,-1,-1):
        sift(i,sl)

    for i in range(sl-1,0,-1):
        swap(i,0)
        sift(0,i)


def unittest():
    print("running unittest...")
    try:
        a = [x for x in range(1000, 0, -1)]
        start = time.time()
        heapsort(a)
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