import math
[x,y,z] = [int(x) for x in input().split()]

print(math.ceil(x/z) * math.ceil(y/z))