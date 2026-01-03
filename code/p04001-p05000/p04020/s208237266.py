import sys,bisect,heapq

mod = 10**9+7
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def IR(n): return([I() for _ in range(n)])
def S(): return(input())

def GCD(a,b):
    while(a%b != 0):
        a,b = b,a%b
    return b

def LCM(a,b):
    return a*b//GCD(a,b)

def main():
    N = I()
    A = IR(N)
    r = 0
    o = 0
    for a in A:
        if o==0:
            r += a//2
            o = a%2
        else:
            if a%2 == 1:
                r += (a+1)//2
                o = 0
            elif a>=2:
                r += a//2
                o = 1
            else:
                o = 0
    return r

if __name__ == "__main__":
    print(main())
