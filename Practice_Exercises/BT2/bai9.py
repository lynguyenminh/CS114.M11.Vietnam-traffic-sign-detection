n = int(input())
for i in range(0,n):
    s = int(input())
    if s == 1:
        print(3)
    elif s == 2:
        print(2)
    elif s == 3:
        print(1)
    elif s % 2 == 0:
        print(0)
    elif s % 2 == 1:
        print(1)