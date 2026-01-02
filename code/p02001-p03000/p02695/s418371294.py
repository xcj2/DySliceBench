import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
 
 
def readstr():
    return input().strip()
 
 
def readint():
    return int(input())
 
 
def readnums():
    return map(int, input().split())
 
 
def readstrs():
    return input().split()
 
 
N, M, Q = readnums()
num_list = [list(readnums()) for _ in range(Q)]
 
ans = 0
for v in combinations_with_replacement(range(1, M + 1), N):
    val = 0
    for n in num_list:
        if v[n[1] - 1] - v[n[0] - 1] == n[2]:
            val += n[3]
    ans = max(ans, val)
 
print(ans)