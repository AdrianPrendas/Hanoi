

o = [4,3,2,1]
a = []
d = []
swp = 0


def hanoi(n, o, a, d):
    print("n: ", n)
    print("o: ", o)
    print("a: ", a)
    print("d: ", d)
    print("-------------")
    if n == 1: 
        if len(o)!=0:
            d.append(o.pop())
    else:
        hanoi(n-1, o, d, a)
        if len(o)!=0:
            d.append(o.pop())
        hanoi(n-1, d, a,o)
    

hanoi(2**len(o)-1, o, a, d)


