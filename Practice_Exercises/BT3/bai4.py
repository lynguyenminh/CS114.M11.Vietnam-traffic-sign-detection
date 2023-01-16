arr = []
[x,y] = [int(x) for x in input().split()]
for i in range(x):
    arr.append([int(x) for x in input().split()])
[t,l,b,r] = [int(x) for x in input().split()]

str_0 = ''
for i in range(y):
    str_0 += '0 '


for i in range(x):
    if  i < t or i > b:
        print(str_0)
        continue
    else:            
        str_line = '0 ' * l
        for z in range(l, r + 1, 1):
            str_line += str(arr[i][z]) + ' '
        str_line += '0 ' * (y - r -1)
        print(str_line)
   