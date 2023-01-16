[a,b] = [int(x) for x in  input().split()]
c = b % a
if (b // a) % 2 == 0:
    d = c
else:
    d = a - c
print(d)