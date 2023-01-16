a = str(input())

a = a.lower()
replace = ('y','u', 'o' ,'e' ,'a', 'i')
for i in a:
    if i in replace:
        a = a.replace(i,'')
b = len(a)
print(a.replace('','.')[0:b*2])