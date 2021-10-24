n = int(input())
k = int(input())
p = int(input())
q = int(input())

# vi tri cua alice
vt1 = (p -1) * 2 + q

# vi tri cua bob
if vt1 - k <=0: 
    if vt1 + k > n: 
        print(-1)
        quit()
    else: 
        vt1 += k
else: 
    vt1 = vt1 - k

if (vt1 / 2).is_integer():
    print(int(vt1/2), 2)
else: 
    print(int(vt1/2 + 0.5), 1)