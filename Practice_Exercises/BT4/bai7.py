[x,y] = [int(i) for i in input().split()]
temp = pow(10, len(str(x)))
n = y // temp
print(n + 1 if y % temp >= x else n)
