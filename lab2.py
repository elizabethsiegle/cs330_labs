import random
import time
import sys
import ctypes

NOT_FOUND = -1

def linearSearch(A, n, x):
    ans = NOT_FOUND;
    for i in range(n):
        if A[i] == x:
            ans = i
    return ans

def betterLinearSearch(A, n, x):
    for i in range(n):
        if A[i] == x:
            return i
    return NOT_FOUND

def SentinelLinearSearch(A, n, x):
    last = A[n-1]
    A[n-1] = x
    i = 0
    while A[i] != x:
        i += 1
    A[n-1] = last
    if (i < n-1) or (A[n-1] == x):
        return i
    else:
        return NOT_FOUND
        
def RecursiveLinearSearch(A, n, i, x):
    #print(i)
    if i >= n:
        return NOT_FOUND
    if A[i] == x:
        return i
    else:
        return RecursiveLinearSearch(A, n, i+1, x)

def test():    
    N = 50000000
    bN = 1000000
    sys.setrecursionlimit(100000000)

    print("recursion limit: ", sys.getrecursionlimit())

    #A = [i for i in range(N)]

    A = [random.randrange(N) for i in range(N)]
    x_best = A[0]
    x_average = random.randrange(N)
    x_worst = NOT_FOUND

    '''
    print("Best cases:")
    start = time.time()
    print("linearSearch ", linearSearch(A, N, x_best))
    duration  = time.time() - start
    print("duration: ", duration)

    start = time.time()
    print("betterLinearSearch ", betterLinearSearch(A, N, x_best))
    duration  = time.time() - start
    print("duration: ", duration)

    start = time.time()
    print("SentinelLinearSearch ", SentinelLinearSearch(A, N, x_best))
    duration  = time.time() - start
    print("duration: ", duration)

    start = time.time()
    print("RecursiveLinearSearch ", RecursiveLinearSearch(A, N, 0, x_best))        
    duration  = time.time() - start
    print("duration: ", duration)
    print()

    print("Average cases:")
    start = time.time()
    print("linearSearch ", linearSearch(A, N, x_average))
    duration  = time.time() - start
    print("duration: ", duration)

    start = time.time()
    print("betterLInearSearch ", betterLInearSearch(A, N, x_average))
    duration  = time.time() - start
    print("duration: ", duration)

    start = time.time()
    print("SentinelLinearSearch ", SentinelLinearSearch(A, N, x_average))
    duration  = time.time() - start
    print("duration: ", duration)

    start = time.time()
    print("RecursiveLinearSearch ", RecursiveLinearSearch(A, N, 0, x_average))        
    duration  = time.time() - start
    print("duration: ", duration)
    print()

    print("Worst cases:")
    #start = time.time()
    #print("linearSearch ", linearSearch(A, N, x_worst))
    #duration  = time.time() - start
    #print("duration: ", duration)

    start = time.time()
    print("betterLInearSearch ", betterLInearSearch(A, N, x_worst))
    duration  = time.time() - start
    print("duration: ", duration)

    start = time.time()
    print("betterLInearSearchv2bn ", betterLInearSearch(A, bN, x_worst))
    duration  = time.time() - start
    print("duration: ", duration)


    #start = time.time()
    #print("SentinelLinearSearch ", SentinelLinearSearch(A, N, x_worst))
    #duration  = time.time() - start
    #print("duration: ", duration)
    
      start = time.time()
      print("betterLInearSearch ", betterLinearSearch(A, N, x_worst))
      duration  = time.time() - start
      print("duration: ", duration)
    print("Searching...")
    start = time.time()
    result = RecursiveLinearSearch(A, N, 0, x_worst)      
    duration  = time.time() - start
    print("RecursiveLinearSearch ", result)  
    print("duration: ", duration)
    print()
   '''

    while bN <= N:
      start = time.time()
     # print("betterLInearSearchv2bn ", betterLinearSearch(A, bN, x_worst))
      duration  = time.time() - start
      print(bN)
      print( duration)
      bN += 1000000
      print("char", ctypes.sizeof('a'))
      print("int", ctypes.sizeof(int))
      print("float", ctypes.sizeof(float))
test()
