def isOdd(n):
    return n%2 == 1

def isOdd2(n):
    return n & 1 != 0

for i in range(-5, 6, 1):
    print(i, isOdd(i))

for j in range(-5, 6, 1):
    print(j, isOdd2(j))

	


