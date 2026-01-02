import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():

    N = I()
    A = LI()
    mod = 10 ** 9 + 7
    sum_ = 0
    D = []
    for i in range(N):
        a = A[i]
        sum_ += a
        D.append(a ** 2)
    ans = (sum_ ** 2 - sum(D)) // 2
    print(ans % mod)










if __name__ == "__main__":
    main()