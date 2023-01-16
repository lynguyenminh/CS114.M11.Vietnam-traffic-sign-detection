a = []
kq = []
import sys
input = sys.stdin.readline

while True:
    a = [int(x) for x in input().split()]
    if a[0] == 0:
        kq.insert(0,a[1])
    elif a[0] == 1:
        kq.append(a[1])
    elif a[0] == 2:
        i = -1
        for j in range(len(kq)):
            if kq[j] == a[1]:
                i = j
                break
        kq.insert(i + 1,a[2])
    elif a[0] == 3:
        for j in range(len(kq)):
            if kq[j] == a[1]:
                kq.pop(j)
                break
    elif a[0] == 4:
        i = len(kq) - 1
        while i >= 0:
            if kq[i] == a[1]:
                kq.pop(i)
            i-=1
    elif a[0] == 5:
        if len(kq) > 0:
            kq.pop(0)
    elif a[0] == 6:
        for k in kq:
            print(k,"", end='')
        break