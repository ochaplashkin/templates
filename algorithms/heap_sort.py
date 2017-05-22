import time

def heapsort(s):
    "Algorithm heap sort"
    sl = len(s)

    def swap(pi,ci):
        "Функция обмена в массиве'"
        if s[pi] < s[ci]:
            s[pi], s[ci] = s[ci], s[pi]

    def siftDown(pi,unsorted):
        """Функция пробегает по пирамиде восстанавливая ее
        также используется для начального создания пирамиды.
        (пробежит по всем потомкам и
         найдет нужное место для следующего элемента)
        """
        i_qt = lambda a,b: a if s[a]>s[b] else b
        while pi*2 + 2 < unsorted:
            qtci = i_qt(pi*2+1,pi*2+2)#выбор наибольшего(левый или правый потомок)
            swap(pi,qtci) #обмен
            pi = qtci

    #собираем пирамиду из массива
    for i in  range(int((sl/2))-1,-1,-1):
        siftDown(i,sl)
    #пирамида собрана
    #сортировка
    for i in range(sl-1,0,-1):
        swap(i,0)#перемещаем верхушку в начало отсортированного списка
        siftDown(0,i)#находим нужное место для нового элемента


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