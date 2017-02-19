import sys
import random
import time
def lol():
    timing = 1
    FLOPS = 0
    b = random.uniform(-1000000, 1000000)
    c = random.uniform(-1000000, 1000000)
    d = random.uniform(-1000000, 1000000)
    e = random.uniform(-1000000, 1000000)
    f = random.uniform(-1000000, 1000000)

    if(e == 0):
        e = e +1
    while(timing >= 0):
        start = time.time()
        a = b*c - d/e + f
        a = b*c - d/e + f
        a = b*c - d/e + f
        a = b*c - d/e + f
        a = b*c - d/e + f
        end = time.time()
        timing = timing - (end - start)
        FLOPS = FLOPS + 20
    print("FLOPS = ", FLOPS)
lol()


