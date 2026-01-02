import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def comb(n):
    return int(n*(n-1)/2)

def main():
    N = I()
    A_list = LI()
    A_ctr = collections.Counter(A_list)
    base = 0
    for i in range(1,N+1):
        base += comb(A_ctr[i])
    for i in range(1,N+1):
        i_val = A_ctr[A_list[i-1]]
        before = comb(i_val)
        after = comb(i_val-1)
        print(int(base - before + after))
main()
