n = int(input())
list = []
while n > 0:
    [a, b] = [int(x) for x in input().split()]
    list.append([int(x) for x in input().split()].count(b))
    n = n -1
for i in list:
    print(i)