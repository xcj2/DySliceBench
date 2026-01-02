import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n = I()
    if n < 30:
        s = ''
        for i in range(1, 100):
            if i % 15 == 0:
                s += 'FizzBuzz'
            elif i % 5 == 0:
                s += 'Buzz'
            elif i % 3 == 0:
                s += 'Fizz'
            else:
                s += str(i)
        # print(s)
        return s[n-1:n+19]
    i = 2
    n -= 4 * 4 + 5
    while 1:
        t = 10**i - (10**(i-1))
        s3 = t // 3
        s5 = t // 5
        s15 = t // 15
        sl = s3 + s5 - s15
        tl = (s3 + s5) * 4 + (t - sl) * i
        if tl >= n:
            break
        n -= tl
        i += 1

    si = 10**(i-1) - 1
    for j in range(i-1,0,-1):
        t = 10**j
        for k in range(1,10):
            s3 = (si+t) // 3 - si // 3
            s5 = (si+t) // 5 - si // 5
            s15 = (si+t) // 15 - si // 15
            sl = s3 + s5 - s15
            tl = (s3 + s5) * 4 + (t - sl) * i
            if tl >= n:
                break
            n -= tl
            si += t
    # print('si,n',si,n)
    s = ''
    for i in range(si+1,si+100):
        if i % 15 == 0:
            s += 'FizzBuzz'
        elif i % 5 == 0:
            s += 'Buzz'
        elif i % 3 == 0:
            s += 'Fizz'
        else:
            s += str(i)
    # print(s)

    return s[n-1:n+19]


print(main())

