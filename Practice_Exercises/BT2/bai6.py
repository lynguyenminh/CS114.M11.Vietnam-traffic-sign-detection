n = int(input())
if n < 4:
    print("NO")
    quit()
else:
    print("YES" if n % 2 == 0 else "NO")
    quit()