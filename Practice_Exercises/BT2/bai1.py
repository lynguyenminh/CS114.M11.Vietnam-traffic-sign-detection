a = int(input())

len = len(str(a))
sum = 0
for i in str(a):
    sum += int(i) ** len
print(True if sum == a else False)