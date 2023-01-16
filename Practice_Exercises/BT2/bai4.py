s = input()

def iN(a):
    if a.find("etra",-4,len(a)) != -1:
        return 1
    if a.find("etr",-3,len(a)) != -1:
        return 2
    return 0

def iA(a):
    if a.find("liala",-5,len(a)) != -1:
        return 1
    if a.find("lios",-4,len(a)) != -1:
        return 2
    return 0 
def iV(a):
    if a.find("inites",-6,len(a)) != -1:
        return 1
    if a.find("initis",-6,len(a)) != -1:
        return 2
    return 0 
def check(a):
    if iN(a)==0 and iA(a)==0 and iV(a)==0:
        return 0
    return 1
def Lan(s):
    arr = s.split(" ")
    while "" in arr:
        arr.remove("")
#kiem tra tu hop le
    for k in arr:
        if check(k) == 0:
           return 0
    if len(arr) <= 1:
        return 1
    sex = 0
    vt = 0

#kiem tra danh tu
    dem = 0
    for k in range (len(arr)):
        if iN(arr[k])==1:
            dem += 1
            sex = 1
            vt = k
        elif iN(arr[k])==2:
            dem += 1
            sex = 2
            vt = k
    if dem != 1:
         return 0


#kiem tra tinh tu:
    for k in range(vt):
        if iA(arr[k])!=sex:
            return 0

#kiem tra dong tu:
    for k in range(vt+1, len(arr)):
        if iV(arr[k])!=sex:
            return 0
    return 1
if Lan(s) == 0:
    print("NO")
elif Lan(s) == 1:
    print("YES")