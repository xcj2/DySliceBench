import sys; sys.setrecursionlimit(2147483647); input = sys.stdin.readline
from math import floor, ceil, sqrt, factorial, log
from collections import Counter, defaultdict, deque
from operator import itemgetter
INF = float('inf'); MOD = 10**9+7
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(MI())
def LIR(n): return [LI() for i in range(n)]
def IS(): return input().rstrip()

def main():
    S = IS()
    N = len(S)
    if N%2 == 1:
        a = N//2
        if S[:a] == S[a+1:][::-1]:
            b = (N-1)//4
            if a%2 == 0:
                if S[:b] == S[b:a][::-1]:
                    c = (N+3)//2; d = c+(N-c)//2
                    if (N-c)%2 == 0:
                        if S[c-1:d-1] == S[d:][::-1]:
                            print('Yes')
                            sys.exit()
                        #else: print(7, S, N)
                    else:
                        if S[c-1:d] == S[d:][::-1]:
                            print('Yes')
                            sys.exit()
                        #else: print(6, S, N)
                #else: print(8, S, N)
            else:
                if S[:b] == S[b+1:a][::-1]:
                    c = (N+3)//2; d = c+(N-c)//2
                    if (N-c)%2 == 0:
                        if S[c-1:d-1] == S[d:][::-1]:
                            print('Yes')
                            sys.exit()
                        #else: print(5, S, N)
                    else:
                        if S[c-1:d] == S[d:][::-1]:
                            print('Yes')
                            sys.exit()
                        #else: print(4, S, N)
                #else: print(3, S, N)
        #else: print(2, S, N)
    #else: print(1, S, N)
    print('No')

if __name__ == '__main__':
    main()