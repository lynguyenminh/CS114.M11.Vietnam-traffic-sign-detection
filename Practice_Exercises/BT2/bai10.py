n = int(input())

def handle(str1, str2):
    if len(str1) != len(str2):
        print('NO')
    else: 
        for i in str1: 
            if i in str2: 
                print('YES')
                return
        print('NO')
        
while n > 0: 
    a, b = input(), input()
    handle(a, b)
    n = n -1