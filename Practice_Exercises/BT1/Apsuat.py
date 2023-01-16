result = (float(input()) * 0.453592 / 6.4516)
n = 0
while result * 10 < 1000000: 
    result *= 10
    n +=1

print(result.__round__(0) / (10 ** n))