import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    A, B = LI()
    A_bottom,A_upper = A/0.08,(A+1)/0.08
    B_bottom,B_upper = B/0.10,(B+1)/0.10
    # print(A_bottom,A_upper,B_bottom,B_upper)
    if A_bottom>=B_bottom and A_bottom<B_upper:
        print(int(A_bottom) if A_bottom<=int(A_bottom) else int(A_bottom)+1)
    elif B_bottom>=A_bottom and B_bottom<A_upper:
        print(int(B_bottom) if B_bottom<=int(B_bottom) else int(B_bottom)+1)
    else:
        print(-1)

main()

