import sys
input = sys.stdin.readline
res ={}
while 1:
    arr = list(map(int, input().split()))
    if arr == []:
        break
    elif arr[0] == 0:
        break
    elif arr[0] == 1:
        res[arr[1]] = 1
    elif arr[0] == 2:
        if res.get(arr[1]):
            print(1)
        else:
            print(0)
    else:
        if res.get(arr[1]):
            del res[arr[1]]