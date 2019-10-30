
#import time


A = [4,3,2,1]
B = []
C = []

def log(a,b,c,n):
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("n: ", n)
    print("---------------")
    #time.sleep(1)

def Hanoi(a, b, c, n):
    if n == 0:
        return
    elif n == 1:
        log(a,b,c,n)
        c.append(a.pop())
    elif n == 2:
        log(a,b,c,n)
        b.append(a.pop())
        log(a,b,c,n)
        c.append(a.pop())
        log(a,b,c,n)
        c.append(b.pop())
    else:
        Hanoi(a, c, b, n-1)
        log(a,b,c,n)
        c.append(a.pop())
        Hanoi(b, a, c,n-1)

Hanoi(A, B, C, len(A))

print("c:", C)

