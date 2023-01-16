n = int(input())
arr = [int(x) for x in input().split()]
[a, b] = [int(x) for x in input().split()]
m = 0
n = n - 1
while not (n - m + 1==a) :
    if abs(arr[n]-b) < abs(b - arr[m]):
        m = m + 1
    else:
        n = n - 1
for i in range(m,n+1):
    print(arr[i] ,'',  end='')