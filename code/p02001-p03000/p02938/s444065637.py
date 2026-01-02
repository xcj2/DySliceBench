import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from functools import lru_cache

MOD = 10**9 + 7

def Fsmall(L,R):
    return sum(y-x == x^y for x in range(L,R+1) for y in range(x,min(x+x-1,R)+1))

@lru_cache(None)
def F(L,R):
    # x<=y<2x
    if R-L < 10:
        return Fsmall(L,R)
    f = 0
    # x=2a, y=2b
    f += F((L+1)//2,R//2)
    # x=2a+1,y=2b → これはルール違反
    # x=2a,y=2b+1
    f += F((L+1)//2,(R-1)//2)
    # x=2a+1,y=2b+1
    f += G(L//2,(R-1)//2)
    return f%MOD

def Gsmall(L,R):
    return sum(y-x == x^y for x in range(L,R+1) for y in range(x,min(x+x,R)+1))

@lru_cache(None)
def G(L,R):
    # x<=y<=2x
    if R-L < 10:
        return Gsmall(L,R)
    f = 0
    # x=2a, y=2b
    f += G((L+1)//2,R//2)
    # x=2a+1,y=2b → これはルール違反
    # x=2a,y=2b+1
    f += F((L+1)//2,(R-1)//2)
    # x=2a+1,y=2b+1
    f += G(L//2,(R-1)//2)
    return f%MOD

L,R = map(int,read().split())

answer = F(L,R)
print(answer)