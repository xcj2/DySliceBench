import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def II(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def SI(): return input()
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')

X, Y, Z, K = LI()
A_li = LI()
B_li = LI()
C_li = LI()

A_li = sorted(A_li, reverse=True) + [-INF]
B_li = sorted(B_li, reverse=True) + [-INF]
C_li = sorted(C_li, reverse=True) + [-INF]

from functools import lru_cache

@lru_cache(maxsize=None)
def calc_result(a,b,c):
    return (A_li[a]+B_li[b]+C_li[c])


search_list = [(0,0,0)]
calc_list = [calc_result(0,0,0)]
for i in range(K):
    maximum = max(calc_list)
    print(maximum)
    index = calc_list.index(maximum)
    a, b, c = search_list[index]
    search_list.pop(index)
    calc_list.pop(index)
    if (a+1, b, c) not in search_list:
        search_list.append((a+1,b,c))
        calc_list.append(calc_result(a+1,b,c))
    if (a, b+1, c) not in search_list:
        search_list.append((a,b+1,c))
        calc_list.append(calc_result(a,b+1,c))
    if (a, b, c+1) not in search_list:
        search_list.append((a,b,c+1))
        calc_list.append(calc_result(a,b,c+1))
