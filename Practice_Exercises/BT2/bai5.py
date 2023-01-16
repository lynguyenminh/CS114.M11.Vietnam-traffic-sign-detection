import math
n = int(input())
x = n
arr = []
for i in range (n):
    [a, b] = [ int(x) for x in input().split()]
    c = math.gcd(a,b)
    a //= c
    b //= c
    arr.append(a)
    arr.append(b)

i = 0
while i < 2*n:
    if arr[i+1] != 1:
        print(arr[i],arr[i+1])
    else:
        print(arr[i])
    i += 2