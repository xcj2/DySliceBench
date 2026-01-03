import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

s = list(input())
alphabets = [chr(ord('a')+i) for i in range(26)]

ans = float('inf')
for a in alphabets:
    t = s[:]
    count = 0
    while True:
        b = []
        if t == [a]*len(t):
            ans = min(ans,count)
            break
        else:
            for i in range(len(t)-1):
                if t[i] == a or t[i+1] == a:
                    b.append(a)
                else:
                    b.append('A')
            count += 1
            t = b[:]

print(ans)