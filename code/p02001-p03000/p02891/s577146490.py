def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

def l_s(L):
    return "".join(map(str, L))

import sys
from itertools import groupby as gb

S = input()
K = INT()
g1 = []

if len(set(S)) == 1:
    print(len(S) * K // 2)
    sys.exit()

for _, s in gb(S):
    g1.append(list(s))

tmp = l_s(g1[0]) + l_s(g1[len(g1) - 1])
g2 = []

for _, s in gb(tmp):
    g2.append(list(s))
    
ans = len(g1[0]) // 2 + len(g1[len(g1) - 1]) // 2

for i in range(1, len(g1) - 1):
    ans += (len(g1[i]) // 2) * K

for i in range(len(g2)):
    ans += (len(g2[i]) // 2) * (K - 1)
    
print(ans)