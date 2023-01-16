[a,b] = [int(i) for i in input().split()]
[m,n] = [int(i) for i in input().split()]
arr = []
for i in range(a):
    arr.append([int(x) for x in input().split()])

if a*b == m*n:
    nn = 0
    for i in arr:
        for j in i:
            print(j, end = " ")
            nn += 1
            if nn == n: 
                print()
                nn = 0
else:
    for i in arr:
        for j in i:
            print(j, end = " ")
        print()