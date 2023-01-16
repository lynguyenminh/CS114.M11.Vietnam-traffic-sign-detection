import math

a = int(input())

for i in range(0, a):
    n = int(input())
    sum = 0
    for i in input().split():
        sum += int(i)
    print(math.ceil(sum/n))