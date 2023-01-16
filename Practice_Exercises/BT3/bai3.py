[x,y] = [int(i) for i in input().split()]
numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))
numbers = numbers1 + numbers2
numbers.sort()
for i in numbers:
    print(i, end = " ")