
[a,b] = [int(i) for i in input().split()]
arr = []

for i in range(a):
    arr.append([int(x) for x in input().split()])

idx = []
for i in range(b):
    max = len(str(arr[0][i]))
    for j in range(a):
        if max < len(str(arr[j][i])):
            max = len(str(arr[j][i]))
    idx.append(max + 1)

idx[0] -= 1

def print_square(square):
    for line in square:
        count = 0
        for i in line:            
            print(str(i).rjust(idx[count]), end="")
            count += 1

        print()
    
print_square(arr)
