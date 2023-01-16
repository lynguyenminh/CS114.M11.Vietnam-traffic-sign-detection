f = float(input())
c = (f-32)/1.8
k = c+273.15
l = len(str(int(c)))
if c < 0 :
    l -= 1
c = round(c,6 - l)
if c == int(c):
    c=int(c)
l = len(str(int(k)))
if k < 0 :
    l -= 1
k = round(k,6 - l)
if k == int(k):
    k=int(k)
print(c,k)