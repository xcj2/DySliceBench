import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline
from itertools import combinations_with_replacement
def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    N,M,Q = MI()
    a = [0]*Q
    b = [0]*Q
    c = [0]*Q
    d = [0]*Q
    for i in range(Q):
        a[i],b[i],c[i],d[i] = MI()
    dsum = 0
    max = 0

    l =list(combinations_with_replacement(range(1,M+1), N))
    for j in l:
        j = list(j)
        dsum = 0
        for k in range(Q):
            if j[b[k]-1]-j[a[k]-1] == c[k]:
                dsum += d[k]
        if max < dsum:
            max = dsum 
    print(max)




if __name__ == "__main__":
	main()