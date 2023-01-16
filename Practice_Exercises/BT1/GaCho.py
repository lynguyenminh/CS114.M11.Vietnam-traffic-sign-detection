import math
a = int(input())
b = int(input())
c = int(input())

if a + b <=c or a + c <= b or b + c <=a: 
    print('Khong phai tam giac', end='')
else:    
    if a == b == c: 
        print('Tam giac deu', end='')
    elif a == b or b == c or c== a: 
        print("Tam giac can", end='')
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a: 
        print("Tam giac vuong", end='')
    else: 
        print("Tam giac thuong", end='')

    # tinh dien tich
    p = (a + b + c)/2
    s = math.sqrt(p * (p-a) * (p-b) * (p-c))
    if s == s.__round__(0):
        s = int(s)
    elif s == s.__round__(1):
        s = s.__round__(1)
    else: 
        s = s.__round__(2)
    print(', dien tich = ' + str(s))