n = int(input())
if n == 1 or n == 2:
    print(1)
elif 2 < n < 31:
    F1 = F2 = 1
    F = 0
    for i in range (2,n):
        F = F1 + F2
        F2 = F1
        F1 = F
    print(F)
else:
    print("So %d khong nam trong khoang [1,30]." %n)